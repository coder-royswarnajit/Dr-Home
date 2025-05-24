# api_service.py
"""API service functions for interacting with Perplexity API"""

import requests
import streamlit as st
from config import PERPLEXITY_API_URL, PERPLEXITY_MODEL, TRUSTED_MEDICAL_SOURCES

class PerplexityService:
    """Service class for Perplexity API interactions"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def _create_enhanced_prompt(self, prompt, sources_filter=""):
        """Create enhanced prompt with medical source filtering"""
        sources_text = "\n- ".join(TRUSTED_MEDICAL_SOURCES)
        
        enhanced_prompt = f"""
        {prompt}
        
        Please provide information from trusted medical sources only, including:
        - {sources_text}
        
        {sources_filter}
        
        Always include source citations and emphasize that this is for educational purposes only.
        """
        return enhanced_prompt
    
    def query(self, prompt, sources_filter="", temperature=0.2, max_tokens=1500):
        """Query Perplexity API with medical source filtering"""
        enhanced_prompt = self._create_enhanced_prompt(prompt, sources_filter)
        
        data = {
            "model": PERPLEXITY_MODEL,
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
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            response = requests.post(PERPLEXITY_API_URL, headers=self.headers, json=data)
            response.raise_for_status()
            
            # Update session state for query tracking
            if 'queries_made' not in st.session_state:
                st.session_state.queries_made = 0
            st.session_state.queries_made += 1
            
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {str(e)}")
            return None
    
    def query_symptom(self, symptom, age_group="All ages", severity="All levels", duration="Any duration"):
        """Query for symptom information"""
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
        return self.query(prompt)
    
    def query_drug_interactions(self, drugs):
        """Query for drug interaction information"""
        drugs_list = ', '.join(drugs)
        prompt = f"""
        Check for drug interactions between these medications: {drugs_list}
        
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
        return self.query(prompt)
    
    def query_medical_translation(self, medical_term):
        """Query for medical term translation"""
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
        return self.query(prompt)
    
    def query_document_translation(self, medical_text):
        """Query for medical document translation"""
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
        return self.query(prompt)