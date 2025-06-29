# main.py
"""Enhanced Dr. Home application entry point"""

import streamlit as st
from config import PAGE_CONFIG
from styles import get_custom_css
from utils import (
    show_disclaimer, setup_api_key, show_api_key_warning, 
    show_session_stats, create_feature_showcase, show_quick_stats
)
from pages import symptom_explorer, drug_interaction_checker, medical_translator, health_resources

def setup_page_config():
    """Configure Streamlit page settings"""
    st.set_page_config(**PAGE_CONFIG)

def render_header():
    """Render the enhanced main application header"""
    st.markdown("""
    <div class="main-header fade-in">
        <h1>🏥 Dr. Home</h1>
        <p>Your AI-Powered Health Information Platform</p>
        <p><small>✨ Powered by Perplexity AI • 🔬 Evidence-based • 🏆 Trusted Sources</small></p>
    </div>
    """, unsafe_allow_html=True)

def setup_sidebar():
    """Setup enhanced sidebar navigation and configuration"""
    # Setup API key
    api_key = setup_api_key()
    
    # Navigation with enhanced styling
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); 
                padding: 1rem; border-radius: 12px; margin: 1rem 0; color: white; text-align: center;">
        <h3 style="margin: 0; color: white;">🧭 Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced page selection with icons
    page_options = {
        "🔍 Symptom Explorer": "Symptom Explorer",
        "💊 Drug Interactions": "Drug Interaction Checker", 
        "🏥 Medical Translator": "Medical Translator",
        "📚 Health Resources": "Health Resources"
    }
    
    selected_page = st.sidebar.selectbox(
        "Choose a feature:",
        list(page_options.keys()),
        format_func=lambda x: x
    )
    
    page = page_options[selected_page]
    
    # Session stats
    show_session_stats()
    
    # Additional sidebar enhancements
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
                padding: 1rem; border-radius: 12px; text-align: center;">
        <h4 style="margin: 0; color: #495057;">💡 Quick Tip</h4>
        <p style="margin: 0.5rem 0; color: #6c757d; font-size: 0.9rem;">
            Always consult healthcare professionals for medical advice. This platform is for educational purposes only.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
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

def show_welcome_content():
    """Show enhanced welcome content when no API key is configured"""
    # Quick stats
    show_quick_stats()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature showcase
    create_feature_showcase()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Enhanced call-to-action
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; text-align: center; color: white; margin: 2rem 0;">
        <h2 style="margin: 0 0 1rem 0; color: white;">🚀 Ready to Get Started?</h2>
        <p style="margin: 0; font-size: 1.1rem; opacity: 0.9;">
            Configure your API key in the sidebar and unlock the full power of Dr. Home!
        </p>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Enhanced main application function"""
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
        show_welcome_content()
        return
    
    # Add a success message for configured API
    st.success("🎉 **Dr. Home is ready!** Your API key is configured and all features are unlocked.")
    
    # Route to appropriate page
    route_to_page(page)

if __name__ == "__main__":
    main()