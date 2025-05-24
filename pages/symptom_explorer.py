# pages/symptom_explorer.py
"""Symptom Explorer page functionality"""

import streamlit as st
from api_service import PerplexityService
from utils import show_loading_message, display_sources

def symptom_explorer():
    """Symptom Explorer page"""
    st.header("Symptom Explorer")
    st.write("Get evidence-based information about symptoms from trusted medical sources.")
    
    # Symptom input
    col1, col2 = st.columns([3, 1])
    with col1:
        symptom = st.text_input("Enter a symptom:", placeholder="e.g., headache, chest pain, fatigue")
    with col2:
        search_button = st.button("Explore Symptom", type="primary")
    
    # Additional filters
    with st.expander("Advanced Options"):
        age_group = st.selectbox("Age Group:", ["All ages", "Children", "Adults", "Elderly"])
        severity = st.selectbox("Severity Level:", ["All levels", "Mild", "Moderate", "Severe"])
        duration = st.selectbox("Duration:", ["Any duration", "Acute (< 1 week)", "Subacute (1-4 weeks)", "Chronic (> 4 weeks)"])
    
    if search_button and symptom and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("Searching medical databases..."):
            result = api_service.query_symptom(symptom, age_group, severity, duration)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                st.markdown(f"""
                <div class="symptom-card">
                    <h3>📋 Information about: {symptom.title()}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(content)
                display_sources(result)
    
    elif search_button and symptom and not st.session_state.get('perplexity_api_key'):
        st.error("Please enter your Perplexity API key in the sidebar first.")