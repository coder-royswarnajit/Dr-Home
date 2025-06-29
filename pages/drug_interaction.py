# pages/drug_interaction.py
"""Enhanced Drug Interaction Checker page functionality"""

import streamlit as st
from api_service import PerplexityService
from utils import show_loading_message, format_drug_list

def drug_interaction_checker():
    """Enhanced Drug Interaction Checker page"""
    st.markdown("""
    <div class="fade-in">
        <h1>💊 Drug Interaction Checker</h1>
        <p style="font-size: 1.1rem; color: #6c757d; margin-bottom: 2rem;">
            Check potential interactions between medications using current medical research and clinical databases.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced input methods
    st.markdown("### 📋 **Enter Medications**")
    
    # Tab-based input for better UX
    tab1, tab2 = st.tabs(["🔄 **Two Medications**", "📝 **Multiple Medications**"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            drug1 = st.text_input(
                "First medication:",
                placeholder="e.g., warfarin, aspirin, metformin",
                help="Enter the generic or brand name"
            )
        with col2:
            drug2 = st.text_input(
                "Second medication:",
                placeholder="e.g., ibuprofen, lisinopril, atorvastatin",
                help="Enter the generic or brand name"
            )
        
        drugs_to_check = [drug1, drug2] if drug1 and drug2 else []
    
    with tab2:
        drug_list = st.text_area(
            "Enter medications (one per line):",
            placeholder="warfarin\nibuprofen\nmetformin\naspirin\nlisinopril",
            height=120,
            help="List each medication on a separate line"
        )
        
        if drug_list:
            drugs_to_check = format_drug_list(drug_list)
        else:
            drugs_to_check = []
    
    # Enhanced check button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        check_button = st.button(
            "🔍 Check Interactions", 
            type="primary", 
            use_container_width=True,
            disabled=len(drugs_to_check) < 2
        )
    
    # Show current medications being checked
    if drugs_to_check and len(drugs_to_check) >= 2:
        st.markdown("### 📋 **Medications to Check:**")
        cols = st.columns(min(len(drugs_to_check), 4))
        for i, drug in enumerate(drugs_to_check):
            with cols[i % 4]:
                st.markdown(f"""
                <div style="background: #e3f2fd; padding: 0.5rem; border-radius: 8px; text-align: center; margin: 0.25rem 0;">
                    💊 <strong>{drug.title()}</strong>
                </div>
                """, unsafe_allow_html=True)
    
    # Process interaction check
    if check_button and drugs_to_check and len(drugs_to_check) >= 2 and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("💊 Analyzing drug interactions in medical databases..."):
            result = api_service.query_drug_interactions(drugs_to_check)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                # Enhanced results display
                st.markdown(f"""
                <div class="drug-warning fade-in">
                    <h2>⚠️ Drug Interaction Analysis</h2>
                    <p><strong>Medications analyzed:</strong> {', '.join([drug.title() for drug in drugs_to_check])}</p>
                    <p><strong>Analysis date:</strong> {st.session_state.get('current_date', 'Today')}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Display content
                st.markdown("---")
                st.markdown(content)
                
                # Enhanced safety warnings
                st.markdown("""
                <div class="emergency-card">
                    <h3>🚨 Important Safety Information</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                        <div>
                            <h4>⚠️ Before Making Changes:</h4>
                            <ul>
                                <li>Consult your doctor or pharmacist</li>
                                <li>Never stop medications abruptly</li>
                                <li>Discuss all supplements and OTC drugs</li>
                                <li>Consider timing of medication doses</li>
                            </ul>
                        </div>
                        <div>
                            <h4>🚨 Seek Immediate Help If:</h4>
                            <ul>
                                <li>Severe allergic reactions occur</li>
                                <li>Unusual bleeding or bruising</li>
                                <li>Severe nausea or vomiting</li>
                                <li>Difficulty breathing or swallowing</li>
                            </ul>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Additional resources
                st.markdown("### 📞 **Professional Resources**")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.info("""
                    **👨‍⚕️ Healthcare Providers**
                    - Your prescribing doctor
                    - Clinical pharmacist
                    - Specialist consultants
                    """)
                
                with col2:
                    st.info("""
                    **📞 Emergency Contacts**
                    - Emergency: 911
                    - Poison Control: 1-800-222-1222
                    - Pharmacy consultation line
                    """)
                
                with col3:
                    st.info("""
                    **🔍 Additional Tools**
                    - Drug interaction databases
                    - Medication management apps
                    - Pharmacy consultation services
                    """)
    
    elif check_button and len(drugs_to_check) < 2:
        st.warning("📝 Please enter at least two medications to check for interactions.")
    
    elif check_button and not st.session_state.get('perplexity_api_key'):
        st.error("🔑 Please configure your Perplexity API key in the sidebar first.")
    
    # Show helpful information when no check is active
    if not check_button:
        st.markdown("### 💡 **Understanding Drug Interactions**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>🔴 Major Interactions</h4>
                <p>Clinically significant interactions that may cause serious adverse effects or reduce medication effectiveness.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <h4>🟡 Moderate Interactions</h4>
                <p>Interactions that may require monitoring, dose adjustments, or timing changes between medications.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>🟢 Minor Interactions</h4>
                <p>Generally mild interactions with minimal clinical significance, but still worth being aware of.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="info-card">
                <h4>💡 Pro Tips</h4>
                <p>Include all medications, supplements, and over-the-counter drugs. Timing of doses can affect interactions.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Common interaction examples
        st.markdown("### 📚 **Common Interaction Examples**")
        
        examples = [
            {"drugs": "Warfarin + Aspirin", "risk": "🔴 High", "effect": "Increased bleeding risk"},
            {"drugs": "ACE Inhibitors + NSAIDs", "risk": "🟡 Moderate", "effect": "Reduced kidney function"},
            {"drugs": "Statins + Grapefruit", "risk": "🟡 Moderate", "effect": "Increased statin levels"},
            {"drugs": "Calcium + Iron", "risk": "🟢 Minor", "effect": "Reduced iron absorption"}
        ]
        
        for example in examples:
            st.markdown(f"""
            <div style="background: #f8f9fa; border-left: 4px solid #dee2e6; padding: 1rem; margin: 0.5rem 0; border-radius: 5px;">
                <strong>{example['drugs']}</strong> - {example['risk']} Risk<br>
                <small>{example['effect']}</small>
            </div>
            """, unsafe_allow_html=True)