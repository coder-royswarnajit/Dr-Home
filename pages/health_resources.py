# pages/health_resources.py
"""Health Resources page functionality"""

import streamlit as st
from config import HEALTH_RESOURCES, EMERGENCY_CONTACTS
from utils import calculate_bmi

def health_resources():
    """Health Resources page"""
    st.header("Health Resources")
    st.write("Access trusted health information and resources.")
    
    # Resource categories
    col1, col2 = st.columns(2)
    
    with col1:
        _render_trusted_sources()
    
    with col2:
        _render_emergency_resources()
    
    # Interactive health calculator
    st.markdown("### Health Calculators")
    _render_health_calculators()

def _render_trusted_sources():
    """Render trusted medical sources section"""
    st.markdown("### Trusted Medical Sources")
    
    # NIH Resources
    st.markdown("**NIH (National Institutes of Health)**")
    for name, url in HEALTH_RESOURCES["NIH"].items():
        st.markdown(f"- [{name}]({url})")
    
    # WHO Resources
    st.markdown("**WHO (World Health Organization)**")
    for name, url in HEALTH_RESOURCES["WHO"].items():
        st.markdown(f"- [{name}]({url})")
    
    # CDC Resources
    st.markdown("**CDC (Centers for Disease Control)**")
    for name, url in HEALTH_RESOURCES["CDC"].items():
        st.markdown(f"- [{name}]({url})")
    
    # Mayo Clinic Resources
    st.markdown("**Mayo Clinic**")
    for name, url in HEALTH_RESOURCES["Mayo Clinic"].items():
        st.markdown(f"- [{name}]({url})")

def _render_emergency_resources():
    """Render emergency resources section"""
    st.markdown("""
    <div class="emergency-card">
        <h3>🚨 Emergency Resources</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"**Emergency Services:** {EMERGENCY_CONTACTS['US']['emergency']} (US), {EMERGENCY_CONTACTS['EU']['emergency']} (EU)")
    st.markdown(f"**Poison Control:** {EMERGENCY_CONTACTS['US']['poison_control']} (US)")
    st.markdown(f"**Crisis Hotline:** {EMERGENCY_CONTACTS['US']['mental_health']} (US Mental Health)")
    st.markdown("**Telemedicine:** Contact your healthcare provider")
    
    st.markdown("""
    ### Health Apps & Tools
    - Symptom checkers (for reference only)
    - Medication reminders
    - Health tracking apps
    - Telehealth platforms
    """)

def _render_health_calculators():
    """Render health calculators section"""
    calc_type = st.selectbox("Choose a calculator:", 
                            ["BMI Calculator", "Heart Rate Zones", "Medication Dosage Info"])
    
    if calc_type == "BMI Calculator":
        _render_bmi_calculator()
    elif calc_type == "Heart Rate Zones":
        _render_heart_rate_calculator()
    elif calc_type == "Medication Dosage Info":
        _render_medication_info()

def _render_bmi_calculator():
    """Render BMI calculator"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        height_ft = st.number_input("Height (feet):", min_value=1, max_value=8, value=5)
        height_in = st.number_input("Height (inches):", min_value=0, max_value=11, value=8)
    
    with col2:
        weight = st.number_input("Weight (lbs):", min_value=50, max_value=500, value=150)
    
    with col3:
        if st.button("Calculate BMI"):
            bmi, category, color = calculate_bmi(height_ft, height_in, weight)
            
            st.markdown(f"""
            <div class="metric-card">
                <h3>Your BMI</h3>
                <h2>{bmi:.1f}</h2>
                <p><strong>{category}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            if color == "info":
                st.info(f"Category: {category}")
            elif color == "success":
                st.success(f"Category: {category}")
            elif color == "warning":
                st.warning(f"Category: {category}")
            else:
                st.error(f"Category: {category}")
            
            st.caption("BMI is a screening tool. Consult healthcare providers for comprehensive health assessment.")

def _render_heart_rate_calculator():
    """Render heart rate zones calculator"""
    age = st.number_input("Enter your age:", min_value=10, max_value=100, value=30)
    
    if st.button("Calculate Heart Rate Zones"):
        max_hr = 220 - age
        
        zones = {
            "Zone 1 (50-60%)": (max_hr * 0.5, max_hr * 0.6),
            "Zone 2 (60-70%)": (max_hr * 0.6, max_hr * 0.7),
            "Zone 3 (70-80%)": (max_hr * 0.7, max_hr * 0.8),
            "Zone 4 (80-90%)": (max_hr * 0.8, max_hr * 0.9),
            "Zone 5 (90-95%)": (max_hr * 0.9, max_hr * 0.95)
        }
        
        st.markdown(f"**Maximum Heart Rate:** {max_hr} bpm")
        st.markdown("**Training Zones:**")
        
        for zone, (lower, upper) in zones.items():
            st.markdown(f"- {zone}: {lower:.0f}-{upper:.0f} bpm")

def _render_medication_info():
    """Render medication dosage information"""
    st.info("""
    **Medication Dosage Information**
    
    This section would typically include:
    - Standard dosing guidelines
    - Age and weight-based calculations
    - Frequency recommendations
    
    **Important:** Always follow your healthcare provider's instructions for medication dosing.
    Never adjust medications without consulting your doctor or pharmacist.
    """)
    
    st.warning("This is a placeholder for medication dosage information. Actual content would be provided by a medical professional.")