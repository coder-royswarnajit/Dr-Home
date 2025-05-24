# pages/drug_interaction.py
"""Drug Interaction Checker page functionality"""

import streamlit as st
from api_service import PerplexityService
from utils import show_loading_message, format_drug_list

def drug_interaction_checker():
    """Drug Interaction Checker page"""
    st.header("Drug Interaction Checker")
    st.write("Check potential interactions between medications using current medical research.")
    
    # Drug input
    col1, col2 = st.columns(2)
    with col1:
        drug1 = st.text_input("First medication:", placeholder="e.g., warfarin, aspirin")
    with col2:
        drug2 = st.text_input("Second medication:", placeholder="e.g., ibuprofen, metformin")
    
    # Multiple drug checker
    with st.expander("Check Multiple Medications"):
        drug_list = st.text_area(
            "Enter medications (one per line):",
            placeholder="warfarin\nibuprofen\nmetformin\naspirin"
        )
    
    check_button = st.button("Check Interactions", type="primary")
    
    if check_button and st.session_state.get('perplexity_api_key'):
        drugs_to_check = []
        
        if drug1 and drug2:
            drugs_to_check = [drug1, drug2]
        elif drug_list:
            drugs_to_check = format_drug_list(drug_list)
        
        if drugs_to_check:
            api_service = PerplexityService(st.session_state.perplexity_api_key)
            
            with show_loading_message("Checking drug interactions in medical databases..."):
                result = api_service.query_drug_interactions(drugs_to_check)
                
                if result and 'choices' in result:
                    content = result['choices'][0]['message']['content']
                    
                    st.markdown(f"""
                    <div class="drug-warning">
                        <h3>⚠️ Drug Interaction Analysis</h3>
                        <p><strong>Medications checked:</strong> {', '.join(drugs_to_check)}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(content)
                    
                    st.warning("**Important:** This information is for educational purposes only. Always consult your pharmacist or doctor before making any changes to your medications.")
        else:
            st.warning("Please enter at least two medications to check for interactions.")
    
    elif check_button and not st.session_state.get('perplexity_api_key'):
        st.error("Please enter your Perplexity API key in the sidebar first.")