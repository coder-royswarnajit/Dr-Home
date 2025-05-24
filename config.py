# config.py
"""Configuration settings for Dr. Home application"""

# Perplexity API Configuration
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_MODEL = "llama-3.1-sonar-large-128k-online"

# Streamlit Configuration
PAGE_CONFIG = {
    "page_title": "Dr. Home - Health Information Platform",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Medical Sources for Enhanced Prompts
TRUSTED_MEDICAL_SOURCES = [
    "PubMed/MEDLINE articles",
    "NIH (National Institutes of Health)",
    "WHO (World Health Organization)",
    "CDC (Centers for Disease Control)",
    "Mayo Clinic",
    "WebMD",
    "Medical journals and peer-reviewed research"
]

# Emergency Contact Information
EMERGENCY_CONTACTS = {
    "US": {
        "emergency": "911",
        "poison_control": "1-800-222-1222",
        "mental_health": "988"
    },
    "EU": {
        "emergency": "112"
    }
}

# Health Resources Links
HEALTH_RESOURCES = {
    "NIH": {
        "MedlinePlus": "https://medlineplus.gov",
        "PubMed": "https://pubmed.ncbi.nlm.nih.gov"
    },
    "WHO": {
        "Health Topics": "https://www.who.int/health-topics"
    },
    "CDC": {
        "Health Information": "https://www.cdc.gov"
    },
    "Mayo Clinic": {
        "Diseases & Conditions": "https://www.mayoclinic.org"
    }
}