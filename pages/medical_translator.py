# pages/medical_translator.py
"""Medical Translator page functionality"""

import streamlit as st
from api_service import PerplexityService
from utils import show_loading_message

def medical_translator():
    """Medical Translator page"""
    st.header("Medical Translator")
    st.write("Translate complex medical terms into understandable language.")
    
    # Input options
    tab1, tab2 = st.tabs(["Term Lookup", "Document Translation"])
    
    with tab1:
        _render_term_lookup_tab()
    
    with tab2:
        _render_document_translation_tab()

def _render_term_lookup_tab():
    """Render the term lookup tab"""
    medical_term = st.text_input("Enter a medical term:", placeholder="e.g., myocardial infarction, pneumonia")
    translate_button = st.button("Translate Term", type="primary", key="translate_term")
    
    if translate_button and medical_term and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("Looking up medical term..."):
            result = api_service.query_medical_translation(medical_term)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                st.markdown(f"""
                <div class="info-card">
                    <h3>Translation for: {medical_term}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(content)
    
    elif translate_button and medical_term and not st.session_state.get('perplexity_api_key'):
        st.error("Please enter your Perplexity API key in the sidebar first.")

def _render_document_translation_tab():
    """Render the document translation tab"""
    medical_text = st.text_area(
        "Paste medical text to translate:",
        placeholder="Enter medical report, diagnosis, or complex medical text here...",
        height=150
    )
    translate_doc_button = st.button("Translate Document", type="primary", key="translate_doc")
    
    if translate_doc_button and medical_text and st.session_state.get('perplexity_api_key'):
        api_service = PerplexityService(st.session_state.perplexity_api_key)
        
        with show_loading_message("Translating medical document..."):
            result = api_service.query_document_translation(medical_text)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                st.markdown("### Patient-Friendly Translation:")
                st.markdown(content)
    
    elif translate_doc_button and medical_text and not st.session_state.get('perplexity_api_key'):
        st.error("Please enter your Perplexity API key in the sidebar first.")
    
    elif translate_doc_button and not medical_text:
        st.warning("Please enter some medical text to translate.")