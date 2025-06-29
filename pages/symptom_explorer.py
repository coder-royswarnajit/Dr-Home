# pages/symptom_explorer.py
"""Enhanced Symptom Explorer page functionality"""

import streamlit as st
from api_service import PerplexityService
from utils import show_loading_message, display_sources

def symptom_explorer():
    """Enhanced Symptom Explorer page"""
    st.markdown("""
    <div class="fade-in">
        <h1>🔍 Symptom Explorer</h1>
        <p style="font-size: 1.1rem; color: #6c757d; margin-bottom: 2rem;">
            Get comprehensive, evidence-based information about symptoms from trusted medical sources.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced symptom input section
    st.markdown("### 📝 **Enter Your Symptom**")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        symptom = st.text_input(
            "",
            placeholder="e.g., headache, chest pain, fatigue, dizziness...",
            help="Describe your symptom in simple terms"
        )
    with col2:
        search_button = st.button("🔍 Explore", type="primary", use_container_width=True)
    
    # Enhanced advanced options
    with st.expander("⚙️ **Advanced Search Options**", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age_group = st.selectbox(
                "👥 Age Group:",
                ["All ages", "Children (0-12)", "Teenagers (13-17)", "Adults (18-64)", "Elderly (65+)"],
                help="Filter information by age group"
            )
        
        with col2:
            severity = st.selectbox(
                "📊 Severity Level:",
                ["All levels", "Mild", "Moderate", "Severe"],
                help="Specify the intensity of the symptom"
            )
        
        with col3:
            duration = st.selectbox(
                "⏱️ Duration:",
                ["Any duration", "Acute (< 1 week)", "Subacute (1-4 weeks)", "Chronic (> 4 weeks)"],
                help="How long have you experienced this symptom?"
            )
    
    # Process search
    if search_button and symptom and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("🔍 Searching medical databases for comprehensive information..."):
            result = api_service.query_symptom(symptom, age_group, severity, duration)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                # Enhanced results display
                st.markdown(f"""
                <div class="symptom-card fade-in">
                    <h2>📋 Medical Information: {symptom.title()}</h2>
                    <div style="display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap;">
                        <span style="background: #e3f2fd; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem;">
                            👥 {age_group}
                        </span>
                        <span style="background: #fff3e0; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem;">
                            📊 {severity}
                        </span>
                        <span style="background: #f3e5f5; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem;">
                            ⏱️ {duration}
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Display content in organized sections
                st.markdown("---")
                st.markdown(content)
                
                # Enhanced emergency warning
                st.markdown("""
                <div class="emergency-card">
                    <h3>🚨 When to Seek Emergency Care</h3>
                    <p><strong>Call emergency services immediately if you experience:</strong></p>
                    <ul>
                        <li>🫀 Severe chest pain or difficulty breathing</li>
                        <li>🧠 Sudden severe headache or confusion</li>
                        <li>🩸 Signs of severe bleeding or trauma</li>
                        <li>🤒 High fever with severe symptoms</li>
                        <li>⚡ Loss of consciousness or severe weakness</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                # Display sources
                display_sources(result)
                
                # Additional resources
                st.markdown("### 🔗 **Additional Resources**")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.info("""
                    **📞 Need immediate help?**
                    - Emergency: 911 (US) / 112 (EU)
                    - Poison Control: 1-800-222-1222
                    - Crisis Line: 988
                    """)
                
                with col2:
                    st.info("""
                    **🏥 Next Steps:**
                    - Consult your healthcare provider
                    - Keep a symptom diary
                    - Note any triggers or patterns
                    """)
    
    elif search_button and symptom and not st.session_state.get('perplexity_api_key'):
        st.error("🔑 Please configure your Perplexity API key in the sidebar first.")
    
    elif search_button and not symptom:
        st.warning("📝 Please enter a symptom to explore.")
    
    # Show helpful tips when no search is active
    if not search_button:
        st.markdown("### 💡 **How to Use Symptom Explorer**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>🎯 Be Specific</h4>
                <p>Describe your symptom clearly. Instead of "pain," try "sharp chest pain" or "throbbing headache."</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <h4>⚙️ Use Filters</h4>
                <p>Advanced options help provide more targeted information based on age, severity, and duration.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>📚 Multiple Sources</h4>
                <p>Information comes from trusted medical sources like NIH, WHO, CDC, and Mayo Clinic.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <h4>🏥 Professional Care</h4>
                <p>This tool provides educational information only. Always consult healthcare professionals.</p>
            </div>
            """, unsafe_allow_html=True)