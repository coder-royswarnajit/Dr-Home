import streamlit as st
import requests
import json
import time
from datetime import datetime
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Dr. Home - Health Information Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2E86AB 0%, #A23B72 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-card {
        background-color: #f8f9fa;
        border-left: 4px solid #2E86AB;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .symptom-card {
        background-color: #e3f2fd;
        border: 1px solid #2196f3;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .drug-warning {
        background-color: #ffebee;
        border: 1px solid #f44336;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .source-citation {
        background-color: #f5f5f5;
        border-left: 3px solid #4CAF50;
        padding: 0.5rem;
        margin: 0.5rem 0;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Perplexity API Configuration
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

def query_perplexity(prompt, api_key, sources_filter=""):
    """Query Perplexity API with medical source filtering"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Enhanced prompt with medical source filtering
    enhanced_prompt = f"""
    {prompt}
    
    Please provide information from trusted medical sources only, including:
    - PubMed/MEDLINE articles
    - NIH (National Institutes of Health)
    - WHO (World Health Organization)
    - CDC (Centers for Disease Control)
    - Mayo Clinic
    - WebMD
    - Medical journals and peer-reviewed research
    
    {sources_filter}
    
    Always include source citations and emphasize that this is for educational purposes only.
    """
    
    data = {
        "model": "llama-3.1-sonar-large-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "You are a medical information assistant that provides accurate, evidence-based health information from trusted sources. Always include disclaimers about consulting healthcare professionals and cite your sources."
            },
            {
                "role": "user",
                "content": enhanced_prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1500
    }
    
    try:
        response = requests.post(PERPLEXITY_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {str(e)}")
        return None

def show_disclaimer():
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
    """Setup Perplexity API key"""
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

def symptom_explorer():
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
    
    if search_button and symptom and st.session_state.perplexity_api_key:
        with st.spinner("Searching medical databases..."):
            prompt = f"""
            Provide comprehensive information about the symptom: {symptom}
            
            Please include:
            1. Medical definition and description
            2. Common causes (most frequent reasons)
            3. Serious causes that require immediate medical attention
            4. When to seek emergency care
            5. Typical diagnostic approaches
            6. General management principles
            7. Red flags and warning signs
            
            Consider: Age group: {age_group}, Severity: {severity}, Duration: {duration}
            
            Format the response clearly with headers and bullet points.
            """
            
            result = query_perplexity(prompt, st.session_state.perplexity_api_key)
            
            if result and 'choices' in result:
                content = result['choices'][0]['message']['content']
                
                st.markdown(f"""
                <div class="symptom-card">
                    <h3>📋 Information about: {symptom.title()}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(content)
                
                # Show sources if available
                if 'citations' in result:
                    st.markdown("Sources:")
                    for citation in result['citations']:
                        st.markdown(f"""
                        <div class="source-citation">
                            <strong>{citation.get('title', 'Medical Source')}</strong><br>
                            <a href="{citation.get('url', '#')}" target="_blank">{citation.get('url', 'Source URL')}</a>
                        </div>
                        """, unsafe_allow_html=True)
    
    elif search_button and symptom and not st.session_state.perplexity_api_key:
        st.error("Please enter your Perplexity API key in the sidebar first.")

def drug_interaction_checker():
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
    
    if check_button and st.session_state.perplexity_api_key:
        drugs_to_check = []
        
        if drug1 and drug2:
            drugs_to_check = [drug1, drug2]
        elif drug_list:
            drugs_to_check = [drug.strip() for drug in drug_list.split('\n') if drug.strip()]
        
        if drugs_to_check:
            with st.spinner("Checking drug interactions in medical databases..."):
                prompt = f"""
                Check for drug interactions between these medications: {', '.join(drugs_to_check)}
                
                Please provide:
                1. Major interactions (clinically significant)
                2. Moderate interactions (monitor closely)
                3. Minor interactions (minimal clinical significance)
                4. Mechanism of interaction
                5. Clinical management recommendations
                6. Monitoring parameters
                7. Alternative medications if interactions are severe
                
                Include severity ratings and clinical significance.
                """
                
                result = query_perplexity(prompt, st.session_state.perplexity_api_key)
                
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
    
    elif check_button and not st.session_state.perplexity_api_key:
        st.error("Please enter your Perplexity API key in the sidebar first.")

def medical_translator():
    st.header("Medical Translator")
    st.write("Translate complex medical terms into understandable language.")
    
    # Input options
    tab1, tab2 = st.tabs(["Term Lookup", "Document Translation"])
    
    with tab1:
        medical_term = st.text_input("Enter a medical term:", placeholder="e.g., myocardial infarction, pneumonia")
        translate_button = st.button("Translate Term", type="primary")
        
        if translate_button and medical_term and st.session_state.perplexity_api_key:
            with st.spinner("Looking up medical term..."):
                prompt = f"""
                Explain the medical term: {medical_term}
                
                Please provide:
                1. Simple, easy-to-understand definition
                2. Common name or lay term
                3. Pronunciation guide
                4. What causes this condition
                5. Common symptoms
                6. How it's diagnosed
                7. Treatment options
                8. Prognosis and outlook
                9. Related terms
                
                Use simple language that a patient would understand.
                """
                
                result = query_perplexity(prompt, st.session_state.perplexity_api_key)
                
                if result and 'choices' in result:
                    content = result['choices'][0]['message']['content']
                    
                    st.markdown(f"""
                    <div class="info-card">
                        <h3>Translation for: {medical_term}</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(content)
    
    with tab2:
        medical_text = st.text_area(
            "Paste medical text to translate:",
            placeholder="Enter medical report, diagnosis, or complex medical text here...",
            height=150
        )
        translate_doc_button = st.button("Translate Document", type="primary")
        
        if translate_doc_button and medical_text and st.session_state.perplexity_api_key:
            with st.spinner("Translating medical document..."):
                prompt = f"""
                Translate this medical text into simple, patient-friendly language:
                
                {medical_text}
                
                Please:
                1. Replace medical jargon with simple terms
                2. Explain what each finding means
                3. Highlight important information
                4. Maintain accuracy while improving readability
                5. Add context where helpful
                
                Keep the same structure but make it understandable for patients.
                """
                
                result = query_perplexity(prompt, st.session_state.perplexity_api_key)
                
                if result and 'choices' in result:
                    content = result['choices'][0]['message']['content']
                    
                    st.markdown("Patient-Friendly Translation:")
                    st.markdown(content)

def health_resources():
    st.header("Health Resources")
    st.write("Access trusted health information and resources.")
    
    # Resource categories
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Trusted Medical Sources
        - **NIH (National Institutes of Health)**
          - [MedlinePlus](https://medlineplus.gov)
          - [PubMed](https://pubmed.ncbi.nlm.nih.gov)
        - **WHO (World Health Organization)**
          - [Health Topics](https://www.who.int/health-topics)
        - **CDC (Centers for Disease Control)**
          - [Health Information](https://www.cdc.gov)
        - **Mayo Clinic**
          - [Diseases & Conditions](https://www.mayoclinic.org)
        """)
    
    with col2:
        st.markdown("""
        ### Emergency Resources
        - **Emergency Services:** 911 (US), 112 (EU)
        - **Poison Control:** 1-800-222-1222 (US)
        - **Crisis Hotline:** 988 (US Mental Health)
        - **Telemedicine:** Contact your healthcare provider
        
        ### Health Apps & Tools
        - Symptom checkers (for reference only)
        - Medication reminders
        - Health tracking apps
        - Telehealth platforms
        """)
    
    # Interactive health calculator
    st.markdown("### Health Calculators")
    
    calc_type = st.selectbox("Choose a calculator:", 
                            ["BMI Calculator", "Heart Rate Zones", "Medication Dosage Info"])
    
    if calc_type == "BMI Calculator":
        col1, col2, col3 = st.columns(3)
        with col1:
            height_ft = st.number_input("Height (feet):", min_value=1, max_value=8, value=5)
            height_in = st.number_input("Height (inches):", min_value=0, max_value=11, value=8)
        with col2:
            weight = st.number_input("Weight (lbs):", min_value=50, max_value=500, value=150)
        with col3:
            if st.button("Calculate BMI"):
                height_total_inches = (height_ft * 12) + height_in
                bmi = (weight * 703) / (height_total_inches ** 2)
                
                st.metric("Your BMI", f"{bmi:.1f}")
                
                if bmi < 18.5:
                    st.info("Underweight")
                elif 18.5 <= bmi < 25:
                    st.success("Normal weight")
                elif 25 <= bmi < 30:
                    st.warning("Overweight")
                else:
                    st.error("Obese")
                
                st.caption("BMI is a screening tool. Consult healthcare providers for comprehensive health assessment.")

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>Dr. Home</h1>
        <p>Your AI-Powered Health Information Platform</p>
        <p><small>Powered by Perplexity AI • Evidence-based • Trusted Sources</small></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Setup API key
    api_key = setup_api_key()
    
    # Show disclaimer
    show_disclaimer()
    
    if not api_key:
        st.warning("⚠️ Please configure your Perplexity API key in the sidebar to use Dr. Home features.")
        st.info("""
        **To get started:**
        1. Visit [Perplexity.ai](https://perplexity.ai) and create an account
        2. Get your API key from the developer settings
        3. Enter the API key in the sidebar
        4. Start exploring health information!
        """)
        return
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a feature:",
        ["Symptom Explorer", "Drug Interaction Checker", "Medical Translator", "Health Resources"]
    )
    
    # Add usage stats
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Session Stats")
    if 'queries_made' not in st.session_state:
        st.session_state.queries_made = 0
    st.sidebar.metric("Queries Made", st.session_state.queries_made)
    
    # Route to appropriate page
    if page == "Symptom Explorer":
        symptom_explorer()
    elif page == "Drug Interaction Checker":
        drug_interaction_checker()
    elif page == "Medical Translator":
        medical_translator()
    elif page == "Health Resources":
        health_resources()

if __name__ == "__main__":
    main()