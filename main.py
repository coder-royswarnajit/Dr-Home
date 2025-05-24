# app.py
"""Main Dr. Home application entry point"""

import streamlit as st
from config import PAGE_CONFIG
from styles import get_custom_css
from utils import show_disclaimer, setup_api_key, show_api_key_warning, show_session_stats
from pages import symptom_explorer, drug_interaction_checker, medical_translator, health_resources

def setup_page_config():
    """Configure Streamlit page settings"""
    st.set_page_config(**PAGE_CONFIG)

def render_header():
    """Render the main application header"""
    st.markdown("""
    <div class="main-header">
        <h1>Dr. Home</h1>
        <p>Your AI-Powered Health Information Platform</p>
        <p><small>Powered by Perplexity AI • Evidence-based • Trusted Sources</small></p>
    </div>
    """, unsafe_allow_html=True)

def setup_sidebar():
    """Setup sidebar navigation and configuration"""
    # Setup API key
    api_key = setup_api_key()
    
    # Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a feature:",
        ["Symptom Explorer", "Drug Interaction Checker", "Medical Translator", "Health Resources"]
    )
    
    # Session stats
    show_session_stats()
    
    return api_key, page

def route_to_page(page):
    """Route to the appropriate page based on selection"""
    if page == "Symptom Explorer":
        symptom_explorer()
    elif page == "Drug Interaction Checker":
        drug_interaction_checker()
    elif page == "Medical Translator":
        medical_translator()
    elif page == "Health Resources":
        health_resources()

def main():
    """Main application function"""
    # Setup page configuration
    setup_page_config()
    
    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Render header
    render_header()
    
    # Setup sidebar and get configuration
    api_key, page = setup_sidebar()
    
    # Show disclaimer
    show_disclaimer()
    
    # Check if API key is configured
    if not api_key:
        show_api_key_warning()
        return
    
    # Route to appropriate page
    route_to_page(page)

if __name__ == "__main__":
    main()