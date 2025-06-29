# pages/health_resources.py
"""Enhanced Health Resources page functionality"""

import streamlit as st
from config import HEALTH_RESOURCES, EMERGENCY_CONTACTS
from utils import calculate_bmi

def health_resources():
    """Enhanced Health Resources page"""
    st.markdown("""
    <div class="fade-in">
        <h1>📚 Health Resources</h1>
        <p style="font-size: 1.1rem; color: #6c757d; margin-bottom: 2rem;">
            Access trusted health information, emergency contacts, and interactive health tools.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced resource categories with tabs
    tab1, tab2, tab3 = st.tabs(["🏥 **Trusted Sources**", "🚨 **Emergency Info**", "🧮 **Health Calculators**"])
    
    with tab1:
        _render_enhanced_trusted_sources()
    
    with tab2:
        _render_enhanced_emergency_resources()
    
    with tab3:
        _render_enhanced_health_calculators()

def _render_enhanced_trusted_sources():
    """Render enhanced trusted medical sources section"""
    st.markdown("### 🏥 **Trusted Medical Sources**")
    st.markdown("Access reliable, evidence-based health information from these authoritative sources:")
    
    # Create cards for each source category
    sources_data = [
        {
            "title": "🏛️ NIH (National Institutes of Health)",
            "description": "The nation's medical research agency, providing comprehensive health information.",
            "links": HEALTH_RESOURCES["NIH"],
            "color": "#2196f3"
        },
        {
            "title": "🌍 WHO (World Health Organization)", 
            "description": "Global health authority providing international health guidance and information.",
            "links": HEALTH_RESOURCES["WHO"],
            "color": "#4caf50"
        },
        {
            "title": "🛡️ CDC (Centers for Disease Control)",
            "description": "Leading national public health institute providing disease prevention information.",
            "links": HEALTH_RESOURCES["CDC"],
            "color": "#ff9800"
        },
        {
            "title": "🏥 Mayo Clinic",
            "description": "Renowned medical institution offering patient care information and health resources.",
            "links": HEALTH_RESOURCES["Mayo Clinic"],
            "color": "#9c27b0"
        }
    ]
    
    for source in sources_data:
        st.markdown(f"""
        <div class="info-card fade-in" style="border-left-color: {source['color']};">
            <h4>{source['title']}</h4>
            <p>{source['description']}</p>
            <div style="margin-top: 1rem;">
        """, unsafe_allow_html=True)
        
        for name, url in source['links'].items():
            st.markdown(f"🔗 [{name}]({url})")
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Additional resources
    st.markdown("### 📖 **Additional Medical Resources**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">🔬</span>
            <div class="feature-title">Research Databases</div>
            <div class="feature-description">
                • PubMed - Medical literature database<br>
                • Cochrane Library - Systematic reviews<br>
                • ClinicalTrials.gov - Clinical trial information
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <span class="feature-icon">📱</span>
            <div class="feature-title">Health Apps & Tools</div>
            <div class="feature-description">
                • Symptom checkers (reference only)<br>
                • Medication reminder apps<br>
                • Health tracking applications<br>
                • Telehealth platforms
            </div>
        </div>
        """, unsafe_allow_html=True)

def _render_enhanced_emergency_resources():
    """Render enhanced emergency resources section"""
    st.markdown("""
    <div class="emergency-card fade-in">
        <h2>🚨 Emergency Resources</h2>
        <p><strong>Keep these numbers readily available for medical emergencies</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Emergency contacts in organized cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); border-color: #f44336;">
            <h3 style="color: #c62828;">🚨 Emergency Services</h3>
            <h2 style="color: #c62828;">{EMERGENCY_CONTACTS['US']['emergency']}</h2>
            <p><strong>United States</strong></p>
            <hr style="border-color: #f44336;">
            <h2 style="color: #c62828;">{EMERGENCY_CONTACTS['EU']['emergency']}</h2>
            <p><strong>European Union</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%); border-color: #4caf50;">
            <h3 style="color: #2e7d32;">☎️ Specialized Help</h3>
            <p><strong>Poison Control:</strong><br>{EMERGENCY_CONTACTS['US']['poison_control']}</p>
            <p><strong>Mental Health Crisis:</strong><br>{EMERGENCY_CONTACTS['US']['mental_health']}</p>
            <p><strong>Telehealth:</strong><br>Contact your healthcare provider</p>
        </div>
        """, unsafe_allow_html=True)
    
    # When to call emergency services
    st.markdown("### 🚨 **When to Call Emergency Services**")
    
    emergency_situations = [
        {"icon": "🫀", "situation": "Chest Pain", "description": "Severe chest pain, pressure, or discomfort"},
        {"icon": "🧠", "situation": "Stroke Signs", "description": "Sudden weakness, confusion, or speech problems"},
        {"icon": "🫁", "situation": "Breathing Issues", "description": "Severe difficulty breathing or shortness of breath"},
        {"icon": "🩸", "situation": "Severe Bleeding", "description": "Uncontrolled bleeding or major trauma"},
        {"icon": "🤒", "situation": "High Fever", "description": "Very high fever with severe symptoms"},
        {"icon": "⚡", "situation": "Loss of Consciousness", "description": "Fainting, seizures, or unresponsiveness"}
    ]
    
    cols = st.columns(3)
    for i, situation in enumerate(emergency_situations):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background: #fff3e0; border: 1px solid #ff9800; border-radius: 8px; padding: 1rem; margin: 0.5rem 0; text-align: center;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{situation['icon']}</div>
                <h5 style="color: #e65100; margin: 0.5rem 0;">{situation['situation']}</h5>
                <p style="margin: 0; font-size: 0.9rem; color: #6c757d;">{situation['description']}</p>
            </div>
            """, unsafe_allow_html=True)

def _render_enhanced_health_calculators():
    """Render enhanced health calculators section"""
    st.markdown("### 🧮 **Interactive Health Calculators**")
    st.markdown("Use these tools to calculate important health metrics and understand your results.")
    
    calc_type = st.selectbox(
        "Choose a calculator:",
        ["📊 BMI Calculator", "❤️ Heart Rate Zones", "💧 Hydration Calculator", "🍎 Calorie Needs"],
        help="Select a health calculator to use"
    )
    
    if calc_type == "📊 BMI Calculator":
        _render_enhanced_bmi_calculator()
    elif calc_type == "❤️ Heart Rate Zones":
        _render_enhanced_heart_rate_calculator()
    elif calc_type == "💧 Hydration Calculator":
        _render_hydration_calculator()
    elif calc_type == "🍎 Calorie Needs":
        _render_calorie_calculator()

def _render_enhanced_bmi_calculator():
    """Render enhanced BMI calculator"""
    st.markdown("#### 📊 **Body Mass Index (BMI) Calculator**")
    st.markdown("Calculate your BMI to understand your weight status relative to your height.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📏 Height**")
        height_ft = st.number_input("Feet:", min_value=1, max_value=8, value=5, key="height_ft")
        height_in = st.number_input("Inches:", min_value=0, max_value=11, value=8, key="height_in")
    
    with col2:
        st.markdown("**⚖️ Weight**")
        weight = st.number_input("Weight (lbs):", min_value=50, max_value=500, value=150, key="weight")
    
    with col3:
        st.markdown("**🧮 Calculate**")
        if st.button("Calculate BMI", type="primary", use_container_width=True):
            bmi, category, color = calculate_bmi(height_ft, height_in, weight)
            
            st.markdown(f"""
            <div class="metric-card fade-in">
                <h3>Your BMI Result</h3>
                <h1 style="font-size: 3rem; margin: 1rem 0;">{bmi:.1f}</h1>
                <h3>{category}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # BMI categories explanation
            st.markdown("#### 📋 **BMI Categories**")
            categories = [
                {"range": "Below 18.5", "category": "Underweight", "color": "#2196f3"},
                {"range": "18.5 - 24.9", "category": "Normal weight", "color": "#4caf50"},
                {"range": "25.0 - 29.9", "category": "Overweight", "color": "#ff9800"},
                {"range": "30.0 and above", "category": "Obese", "color": "#f44336"}
            ]
            
            for cat in categories:
                highlight = "font-weight: bold; background: #f0f0f0;" if cat["category"].lower() in category.lower() else ""
                st.markdown(f"""
                <div style="border-left: 4px solid {cat['color']}; padding: 0.5rem; margin: 0.25rem 0; {highlight}">
                    <strong>{cat['range']}</strong> - {cat['category']}
                </div>
                """, unsafe_allow_html=True)
            
            st.caption("⚠️ BMI is a screening tool. Consult healthcare providers for comprehensive health assessment.")

def _render_enhanced_heart_rate_calculator():
    """Render enhanced heart rate zones calculator"""
    st.markdown("#### ❤️ **Heart Rate Training Zones Calculator**")
    st.markdown("Calculate your target heart rate zones for different types of exercise.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Enter your age:", min_value=10, max_value=100, value=30)
    
    with col2:
        if st.button("Calculate Heart Rate Zones", type="primary", use_container_width=True):
            max_hr = 220 - age
            
            st.markdown(f"""
            <div class="metric-card">
                <h3>Maximum Heart Rate</h3>
                <h2>{max_hr} bpm</h2>
            </div>
            """, unsafe_allow_html=True)
    
    if 'max_hr' in locals():
        st.markdown("#### 🎯 **Training Zones**")
        
        zones = [
            {"name": "Zone 1: Active Recovery", "range": (50, 60), "color": "#4caf50", "description": "Light activity, warm-up"},
            {"name": "Zone 2: Base Endurance", "range": (60, 70), "color": "#2196f3", "description": "Aerobic base building"},
            {"name": "Zone 3: Aerobic", "range": (70, 80), "color": "#ff9800", "description": "Moderate intensity"},
            {"name": "Zone 4: Threshold", "range": (80, 90), "color": "#f44336", "description": "Hard intensity"},
            {"name": "Zone 5: Neuromuscular", "range": (90, 95), "color": "#9c27b0", "description": "Maximum effort"}
        ]
        
        for zone in zones:
            lower = int(max_hr * zone['range'][0] / 100)
            upper = int(max_hr * zone['range'][1] / 100)
            
            st.markdown(f"""
            <div style="border-left: 4px solid {zone['color']}; padding: 1rem; margin: 0.5rem 0; background: #f8f9fa; border-radius: 5px;">
                <strong>{zone['name']}</strong><br>
                <span style="font-size: 1.2rem; color: {zone['color']};">{lower}-{upper} bpm</span><br>
                <small>{zone['description']}</small>
            </div>
            """, unsafe_allow_html=True)

def _render_hydration_calculator():
    """Render hydration calculator"""
    st.markdown("#### 💧 **Daily Hydration Calculator**")
    st.markdown("Calculate your recommended daily water intake based on your body weight and activity level.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_lbs = st.number_input("Weight (lbs):", min_value=50, max_value=500, value=150)
        activity_level = st.selectbox("Activity Level:", 
                                    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
    
    with col2:
        if st.button("Calculate Water Needs", type="primary", use_container_width=True):
            # Basic calculation: weight in lbs / 2 = ounces of water
            base_water = weight_lbs / 2
            
            # Adjust for activity level
            multipliers = {"Sedentary": 1.0, "Lightly Active": 1.2, "Moderately Active": 1.4, "Very Active": 1.6}
            total_water = base_water * multipliers[activity_level]
            
            cups = total_water / 8  # 8 oz per cup
            liters = total_water * 0.0295735  # Convert oz to liters
            
            st.markdown(f"""
            <div class="metric-card">
                <h3>💧 Daily Water Intake</h3>
                <h2>{total_water:.0f} oz</h2>
                <p>{cups:.1f} cups | {liters:.1f} liters</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.info("💡 This is a general guideline. Adjust based on climate, health conditions, and individual needs.")

def _render_calorie_calculator():
    """Render calorie needs calculator"""
    st.markdown("#### 🍎 **Daily Calorie Needs Calculator**")
    st.markdown("Estimate your daily caloric needs based on age, gender, weight, height, and activity level.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender:", ["Male", "Female"])
        age = st.number_input("Age:", min_value=10, max_value=100, value=30)
        weight_lbs = st.number_input("Weight (lbs):", min_value=50, max_value=500, value=150)
        height_in = st.number_input("Height (inches):", min_value=36, max_value=96, value=68)
    
    with col2:
        activity = st.selectbox("Activity Level:", [
            "Sedentary (little/no exercise)",
            "Light (light exercise 1-3 days/week)",
            "Moderate (moderate exercise 3-5 days/week)",
            "Active (hard exercise 6-7 days/week)",
            "Very Active (very hard exercise, physical job)"
        ])
        
        if st.button("Calculate Calorie Needs", type="primary", use_container_width=True):
            # Convert to metric
            weight_kg = weight_lbs * 0.453592
            height_cm = height_in * 2.54
            
            # Mifflin-St Jeor Equation
            if gender == "Male":
                bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
            else:
                bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
            
            # Activity multipliers
            activity_multipliers = {
                "Sedentary (little/no exercise)": 1.2,
                "Light (light exercise 1-3 days/week)": 1.375,
                "Moderate (moderate exercise 3-5 days/week)": 1.55,
                "Active (hard exercise 6-7 days/week)": 1.725,
                "Very Active (very hard exercise, physical job)": 1.9
            }
            
            total_calories = bmr * activity_multipliers[activity]
            
            st.markdown(f"""
            <div class="metric-card">
                <h3>🍎 Daily Calorie Needs</h3>
                <h2>{total_calories:.0f} calories</h2>
                <p>BMR: {bmr:.0f} calories</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Calorie goals for different objectives
            st.markdown("#### 🎯 **Calorie Goals by Objective**")
            goals = [
                {"goal": "Weight Loss", "calories": total_calories - 500, "color": "#f44336"},
                {"goal": "Maintenance", "calories": total_calories, "color": "#4caf50"},
                {"goal": "Weight Gain", "calories": total_calories + 500, "color": "#2196f3"}
            ]
            
            for goal in goals:
                st.markdown(f"""
                <div style="border-left: 4px solid {goal['color']}; padding: 0.5rem; margin: 0.25rem 0;">
                    <strong>{goal['goal']}:</strong> {goal['calories']:.0f} calories/day
                </div>
                """, unsafe_allow_html=True)
            
            st.caption("⚠️ Consult with a healthcare provider or registered dietitian for personalized nutrition advice.")