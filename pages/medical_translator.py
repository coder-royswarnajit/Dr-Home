# pages/medical_translator.py
"""Enhanced Medical Translator page functionality"""

import streamlit as st
from api_service import PerplexityService
from utils import show_loading_message

def medical_translator():
    """Enhanced Medical Translator page"""
    st.markdown("""
    <div class="fade-in">
        <h1>🏥 Medical Translator</h1>
        <p style="font-size: 1.1rem; color: #6c757d; margin-bottom: 2rem;">
            Transform complex medical terminology into clear, understandable language for patients and families.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced input options with better UX
    tab1, tab2 = st.tabs(["🔍 **Term Lookup**", "📄 **Document Translation**"])
    
    with tab1:
        _render_enhanced_term_lookup_tab()
    
    with tab2:
        _render_enhanced_document_translation_tab()

def _render_enhanced_term_lookup_tab():
    """Render the enhanced term lookup tab"""
    st.markdown("### 🔍 **Medical Term Lookup**")
    st.markdown("Enter any medical term to get a clear, patient-friendly explanation.")
    
    # Enhanced input with suggestions
    col1, col2 = st.columns([4, 1])
    with col1:
        medical_term = st.text_input(
            "",
            placeholder="e.g., myocardial infarction, pneumonia, hypertension...",
            help="Enter the medical term you'd like to understand"
        )
    with col2:
        translate_button = st.button("🔍 Translate", type="primary", key="translate_term", use_container_width=True)
    
    # Common terms quick access
    st.markdown("**💡 Quick Examples:**")
    common_terms = ["Myocardial Infarction", "Pneumonia", "Hypertension", "Diabetes Mellitus", "Osteoarthritis"]
    
    cols = st.columns(len(common_terms))
    for i, term in enumerate(common_terms):
        with cols[i]:
            if st.button(term, key=f"quick_term_{i}", use_container_width=True):
                st.session_state.selected_term = term
                medical_term = term
    
    # Process translation
    if translate_button and medical_term and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("🔍 Looking up medical term and preparing patient-friendly explanation..."):
            result = api_service.query_medical_translation(medical_term)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                # Enhanced results display
                st.markdown(f"""
                <div class="info-card fade-in">
                    <h2>📖 Translation for: {medical_term.title()}</h2>
                    <p style="color: #6c757d; margin: 0;">Patient-friendly explanation from trusted medical sources</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.markdown(content)
                
                # Additional helpful information
                st.markdown("### 🔗 **Additional Resources**")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.info("""
                    **📚 Learn More:**
                    - Ask your healthcare provider
                    - Request printed materials
                    - Join patient education classes
                    """)
                
                with col2:
                    st.info("""
                    **💬 Questions to Ask:**
                    - What does this mean for me?
                    - What are my treatment options?
                    - What should I expect?
                    """)
    
    elif translate_button and medical_term and not st.session_state.get('perplexity_api_key'):
        st.error("🔑 Please configure your Perplexity API key in the sidebar first.")
    
    elif translate_button and not medical_term:
        st.warning("📝 Please enter a medical term to translate.")

def _render_enhanced_document_translation_tab():
    """Render the enhanced document translation tab"""
    st.markdown("### 📄 **Medical Document Translation**")
    st.markdown("Paste complex medical text to get a clear, patient-friendly version.")
    
    # Enhanced text input
    medical_text = st.text_area(
        "**Paste your medical text here:**",
        placeholder="""Example: "Patient presents with acute myocardial infarction with ST elevation in leads II, III, and aVF, consistent with inferior wall STEMI. Troponin levels elevated at 15.2 ng/mL. Recommend immediate cardiac catheterization and PCI."
        
Enter your medical report, diagnosis, lab results, or any complex medical text...""",
        height=200,
        help="Copy and paste text from medical reports, discharge summaries, lab results, etc."
    )
    
    # Enhanced translate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        translate_doc_button = st.button(
            "📄 Translate Document", 
            type="primary", 
            key="translate_doc",
            use_container_width=True,
            disabled=not medical_text
        )
    
    # Character count
    if medical_text:
        st.caption(f"📊 Character count: {len(medical_text)}")
    
    # Process document translation
    if translate_doc_button and medical_text and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("📄 Translating medical document into patient-friendly language..."):
            result = api_service.query_document_translation(medical_text)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                # Enhanced results display with before/after comparison
                st.markdown("### 📋 **Translation Results**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("""
                    <div style="background: #fff3e0; border: 2px solid #ff9800; border-radius: 12px; padding: 1rem;">
                        <h4 style="color: #e65100; margin-top: 0;">📄 Original Medical Text</h4>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander("View Original Text", expanded=False):
                        st.text(medical_text)
                
                with col2:
                    st.markdown("""
                    <div style="background: #e8f5e8; border: 2px solid #4caf50; border-radius: 12px; padding: 1rem;">
                        <h4 style="color: #2e7d32; margin-top: 0;">✨ Patient-Friendly Translation</h4>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display translated content
                st.markdown("---")
                st.markdown(content)
                
                # Additional guidance
                st.markdown("### 💡 **Next Steps**")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.info("""
                    **📞 Discuss with Your Doctor:**
                    - Ask about anything unclear
                    - Request additional explanations
                    - Discuss treatment options
                    """)
                
                with col2:
                    st.info("""
                    **📝 Keep Records:**
                    - Save both versions
                    - Share with family if needed
                    - Bring to appointments
                    """)
                
                with col3:
                    st.info("""
                    **🔍 Research Further:**
                    - Use trusted medical websites
                    - Join patient support groups
                    - Seek second opinions if needed
                    """)
    
    elif translate_doc_button and medical_text and not st.session_state.get('perplexity_api_key'):
        st.error("🔑 Please configure your Perplexity API key in the sidebar first.")
    
    elif translate_doc_button and not medical_text:
        st.warning("📝 Please enter some medical text to translate.")
    
    # Show helpful tips when no translation is active
    if not translate_doc_button:
        st.markdown("### 💡 **Translation Tips**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="info-card">
                <h4>📋 What Can Be Translated</h4>
                <ul>
                    <li>Medical reports and summaries</li>
                    <li>Lab results and test findings</li>
                    <li>Discharge instructions</li>
                    <li>Prescription information</li>
                    <li>Diagnostic explanations</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-card">
                <h4>✨ What You'll Get</h4>
                <ul>
                    <li>Plain English explanations</li>
                    <li>Context for medical findings</li>
                    <li>Simplified terminology</li>
                    <li>Highlighted important information</li>
                    <li>Maintained medical accuracy</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)