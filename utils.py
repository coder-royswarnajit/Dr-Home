# utils.py
"""Enhanced utility functions for Dr. Home application"""

import streamlit as st
from contextlib import contextmanager

def show_disclaimer():
    """Display enhanced medical disclaimer"""
    st.markdown("""
    <div class="warning-box fade-in">
        <h4>⚠️ IMPORTANT MEDICAL DISCLAIMER</h4>
        <p><strong>This platform is for educational purposes only and does not replace professional medical advice.</strong></p>
        <ul>
            <li>🏥 Always consult healthcare professionals for medical concerns</li>
            <li>🚨 In emergencies, call your local emergency number immediately</li>
            <li>🚫 This information should not be used for self-diagnosis or treatment</li>
            <li>💊 Drug interactions shown are for reference only - consult your pharmacist or doctor</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def setup_api_key():
    """Setup Perplexity API key in enhanced sidebar"""
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1rem; border-radius: 12px; margin-bottom: 1rem; color: white; text-align: center;">
        <h3 style="margin: 0; color: white;">🔑 API Configuration</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if API key is already stored in session state
    if 'perplexity_api_key' not in st.session_state:
        st.session_state.perplexity_api_key = ""
    
    api_key = st.sidebar.text_input(
        "Enter your Perplexity API Key:",
        type="password",
        value=st.session_state.perplexity_api_key,
        help="Get your API key from https://perplexity.ai",
        placeholder="pplx-..."
    )
    
    if api_key:
        st.session_state.perplexity_api_key = api_key
        st.sidebar.success("✅ API Key configured!")
        return api_key
    else:
        st.sidebar.warning("⚠️ Please enter your Perplexity API key")
        st.sidebar.info("💡 Get a free API key from [Perplexity.ai](https://perplexity.ai)")
        return None

def show_api_key_warning():
    """Show enhanced warning when API key is not configured"""
    st.markdown("""
    <div class="info-card fade-in">
        <h3>🔐 API Key Required</h3>
        <p>Please configure your Perplexity API key in the sidebar to unlock all Dr. Home features.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🚀</span>
            <div class="feature-title">Quick Setup</div>
            <div class="feature-description">
                Get started in just 3 simple steps with your free Perplexity API key.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🔒</span>
            <div class="feature-title">Secure & Private</div>
            <div class="feature-description">
                Your API key is stored securely and never shared with third parties.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("""
    **📋 Setup Instructions:**
    1. 🌐 Visit [Perplexity.ai](https://perplexity.ai) and create a free account
    2. 🔑 Navigate to API settings and generate your API key
    3. 📝 Enter the API key in the sidebar configuration panel
    4. 🎉 Start exploring evidence-based health information!
    """)

def show_session_stats():
    """Display enhanced session statistics in sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                padding: 1rem; border-radius: 12px; text-align: center;">
        <h4 style="margin: 0; color: #1565c0;">📊 Session Stats</h4>
    </div>
    """, unsafe_allow_html=True)
    
    if 'queries_made' not in st.session_state:
        st.session_state.queries_made = 0
    
    # Enhanced metrics display
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("🔍 Queries", st.session_state.queries_made)
    with col2:
        st.metric("⭐ Session", "Active")

def calculate_bmi(height_ft, height_in, weight):
    """Calculate BMI and return result with enhanced category"""
    height_total_inches = (height_ft * 12) + height_in
    bmi = (weight * 703) / (height_total_inches ** 2)
    
    # Determine category with enhanced styling
    if bmi < 18.5:
        category = "Underweight"
        color = "info"
        emoji = "📉"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "success"
        emoji = "✅"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "warning"
        emoji = "⚠️"
    else:
        category = "Obese"
        color = "error"
        emoji = "🚨"
    
    return bmi, f"{emoji} {category}", color

def format_drug_list(drug_input):
    """Format drug input into a clean list"""
    if isinstance(drug_input, str):
        return [drug.strip() for drug in drug_input.split('\n') if drug.strip()]
    return drug_input

def display_sources(result):
    """Display enhanced source citations if available"""
    if result and 'citations' in result:
        st.markdown("### 📚 **Trusted Sources**")
        for i, citation in enumerate(result['citations'], 1):
            st.markdown(f"""
            <div class="source-citation slide-in">
                <strong>📖 Source {i}: {citation.get('title', 'Medical Source')}</strong><br>
                <a href="{citation.get('url', '#')}" target="_blank" style="color: #667eea; text-decoration: none;">
                    🔗 {citation.get('url', 'Source URL')}
                </a>
            </div>
            """, unsafe_allow_html=True)

@contextmanager
def show_loading_message(message="Processing your request..."):
    """Show an enhanced loading spinner with custom message"""
    with st.spinner(f"🔄 {message}"):
        yield

def create_feature_showcase():
    """Create an enhanced feature showcase for the home page"""
    st.markdown("### 🌟 **Explore Our Features**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card fade-in">
            <span class="feature-icon">🔍</span>
            <div class="feature-title">Symptom Explorer</div>
            <div class="feature-description">
                Get comprehensive, evidence-based information about symptoms from trusted medical sources with advanced filtering options.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card fade-in">
            <span class="feature-icon">🏥</span>
            <div class="feature-title">Medical Translator</div>
            <div class="feature-description">
                Transform complex medical terminology into clear, understandable language for patients and families.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card fade-in">
            <span class="feature-icon">💊</span>
            <div class="feature-title">Drug Interactions</div>
            <div class="feature-description">
                Check potential medication interactions with detailed analysis and clinical recommendations from medical databases.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card fade-in">
            <span class="feature-icon">📚</span>
            <div class="feature-title">Health Resources</div>
            <div class="feature-description">
                Access curated health tools, calculators, and links to trusted medical organizations and emergency contacts.
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_quick_stats():
    """Display quick statistics about the platform"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <h3 style="color: #667eea; margin: 0;">🏥</h3>
            <h4 style="margin: 0.5rem 0;">Trusted Sources</h4>
            <p style="margin: 0; color: #6c757d;">NIH, WHO, CDC, Mayo Clinic</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
            <h3 style="color: #28a745; margin: 0;">🔬</h3>
            <h4 style="margin: 0.5rem 0;">Evidence-Based</h4>
            <p style="margin: 0; color: #6c757d;">Peer-reviewed research</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-container">
            <h3 style="color: #ffc107; margin: 0;">⚡</h3>
            <h4 style="margin: 0.5rem 0;">Real-time</h4>
            <p style="margin: 0; color: #6c757d;">Latest medical information</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-container">
            <h3 style="color: #dc3545; margin: 0;">🔒</h3>
            <h4 style="margin: 0.5rem 0;">Secure</h4>
            <p style="margin: 0; color: #6c757d;">Privacy protected</p>
        </div>
        """, unsafe_allow_html=True)