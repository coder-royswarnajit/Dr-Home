# utils.py
"""Utility functions for Dr. Home application"""

import streamlit as st

def show_disclaimer():
    """Display medical disclaimer"""
    st.markdown("""
    <div class="warning-box">
        <h4>⚠️ IMPORTANT MEDICAL DISCLAIMER</h4>
        <p><strong>This platform is for educational purposes only and does not replace professional medical advice.</strong></p>
        <ul>
            <li>Always consult healthcare professionals for medical concerns</li>
            <li>In emergencies, call your local emergency number immediately</li>
            <li>This information should not be used for self-diagnosis or treatment</li>
            <li>Drug interactions shown are for reference only - consult your pharmacist or doctor</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def setup_api_key():
    """Setup Perplexity API key in sidebar"""
    st.sidebar.header("🔑 API Configuration")
    
    # Check if API key is already stored in session state
    if 'perplexity_api_key' not in st.session_state:
        st.session_state.perplexity_api_key = ""
    
    api_key = st.sidebar.text_input(
        "Enter your Perplexity API Key:",
        type="password",
        value=st.session_state.perplexity_api_key,
        help="Get your API key from https://perplexity.ai"
    )
    
    if api_key:
        st.session_state.perplexity_api_key = api_key
        st.sidebar.success("API Key configured!")
        return api_key
    else:
        st.sidebar.warning("Please enter your Perplexity API key to use the platform")
        st.sidebar.info("You can get a free API key from https://perplexity.ai")
        return None

def show_api_key_warning():
    """Show warning when API key is not configured"""
    st.warning("⚠️ Please configure your Perplexity API key in the sidebar to use Dr. Home features.")
    st.info("""
    **To get started:**
    1. Visit [Perplexity.ai](https://perplexity.ai) and create an account
    2. Get your API key from the developer settings
    3. Enter the API key in the sidebar
    4. Start exploring health information!
    """)

def show_session_stats():
    """Display session statistics in sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Session Stats")
    if 'queries_made' not in st.session_state:
        st.session_state.queries_made = 0
    st.sidebar.metric("Queries Made", st.session_state.queries_made)

def calculate_bmi(height_ft, height_in, weight):
    """Calculate BMI and return result with category"""
    height_total_inches = (height_ft * 12) + height_in
    bmi = (weight * 703) / (height_total_inches ** 2)
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
        color = "info"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "success"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "warning"
    else:
        category = "Obese"
        color = "error"
    
    return bmi, category, color

def format_drug_list(drug_input):
    """Format drug input into a clean list"""
    if isinstance(drug_input, str):
        return [drug.strip() for drug in drug_input.split('\n') if drug.strip()]
    return drug_input

def display_sources(result):
    """Display source citations if available"""
    if result and 'citations' in result:
        st.markdown("**Sources:**")
        for citation in result['citations']:
            st.markdown(f"""
            <div class="source-citation">
                <strong>{citation.get('title', 'Medical Source')}</strong><br>
                <a href="{citation.get('url', '#')}" target="_blank">{citation.get('url', 'Source URL')}</a>
            </div>
            """, unsafe_allow_html=True)

def show_loading_message(message="Processing your request..."):
    """Show a loading spinner with custom message"""
    return st.spinner(message)