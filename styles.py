# styles.py
"""Enhanced CSS styles for Dr. Home application"""

def get_custom_css():
    """Returns enhanced custom CSS for the application"""
    return """
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Styles */
        .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main Header */
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            color: white;
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }
        
        .main-header h1 {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: relative;
            z-index: 1;
        }
        
        .main-header p {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 0.5rem;
            position: relative;
            z-index: 1;
        }
        
        .main-header small {
            font-size: 0.9rem;
            opacity: 0.8;
            position: relative;
            z-index: 1;
        }
        
        /* Enhanced Warning Box */
        .warning-box {
            background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
            border: 2px solid #ffc107;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 25px rgba(255, 193, 7, 0.15);
            position: relative;
        }
        
        .warning-box::before {
            content: '⚠️';
            position: absolute;
            top: -10px;
            left: 20px;
            background: #ffc107;
            padding: 8px 12px;
            border-radius: 50%;
            font-size: 1.2rem;
        }
        
        .warning-box h4 {
            color: #e65100;
            margin-top: 0;
            font-weight: 600;
            margin-left: 20px;
        }
        
        /* Enhanced Cards */
        .info-card {
            background: linear-gradient(135deg, #f8f9ff 0%, #e3f2fd 100%);
            border: none;
            border-left: 5px solid #2196f3;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 25px rgba(33, 150, 243, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(33, 150, 243, 0.15);
        }
        
        .symptom-card {
            background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
            border: 2px solid #4caf50;
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 10px 30px rgba(76, 175, 80, 0.15);
            position: relative;
            overflow: hidden;
        }
        
        .symptom-card::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            transform: rotate(45deg);
        }
        
        .symptom-card h3 {
            color: #2e7d32;
            margin-bottom: 1rem;
            font-weight: 600;
            position: relative;
            z-index: 1;
        }
        
        .drug-warning {
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            border: 2px solid #f44336;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 0 8px 25px rgba(244, 67, 54, 0.15);
            position: relative;
        }
        
        .drug-warning::before {
            content: '💊';
            position: absolute;
            top: -10px;
            left: 20px;
            background: #f44336;
            padding: 8px 12px;
            border-radius: 50%;
            font-size: 1.2rem;
        }
        
        .drug-warning h3 {
            color: #c62828;
            margin-left: 20px;
            font-weight: 600;
        }
        
        /* Enhanced Source Citations */
        .source-citation {
            background: linear-gradient(135deg, #f1f8e9 0%, #dcedc8 100%);
            border-left: 4px solid #8bc34a;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            font-size: 0.9em;
            box-shadow: 0 4px 15px rgba(139, 195, 74, 0.1);
            transition: transform 0.2s ease;
        }
        
        .source-citation:hover {
            transform: translateX(5px);
        }
        
        /* Enhanced Metric Card */
        .metric-card {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            border: 2px solid #2196f3;
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            text-align: center;
            box-shadow: 0 10px 30px rgba(33, 150, 243, 0.15);
            transition: transform 0.3s ease;
        }
        
        .metric-card:hover {
            transform: scale(1.02);
        }
        
        .metric-card h2 {
            font-size: 3rem;
            font-weight: 700;
            color: #1976d2;
            margin: 0.5rem 0;
            text-shadow: 0 2px 4px rgba(25, 118, 210, 0.1);
        }
        
        .metric-card h3 {
            color: #1565c0;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        
        /* Emergency Card */
        .emergency-card {
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            border: 3px solid #f44336;
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(244, 67, 54, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .emergency-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, #f44336, #e91e63, #f44336);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        
        .emergency-card h3 {
            color: #c62828;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        
        /* Enhanced Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Enhanced Input Fields */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.3s ease;
            background: white;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > select:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            outline: none;
        }
        
        /* Enhanced Sidebar */
        .css-1d391kg {
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
            border-right: 1px solid #dee2e6;
        }
        
        /* Enhanced Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: #f8f9fa;
            border-radius: 12px;
            padding: 4px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        /* Enhanced Expander */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 12px;
            padding: 1rem;
            font-weight: 600;
            border: 1px solid #dee2e6;
        }
        
        /* Enhanced Metrics */
        .metric-container {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            border: 1px solid #e9ecef;
        }
        
        /* Loading Spinner Enhancement */
        .stSpinner > div {
            border-top-color: #667eea !important;
        }
        
        /* Enhanced Success/Error Messages */
        .stSuccess {
            background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
            border: 1px solid #4caf50;
            border-radius: 12px;
            padding: 1rem;
        }
        
        .stError {
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            border: 1px solid #f44336;
            border-radius: 12px;
            padding: 1rem;
        }
        
        .stWarning {
            background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
            border: 1px solid #ffc107;
            border-radius: 12px;
            padding: 1rem;
        }
        
        .stInfo {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            border: 1px solid #2196f3;
            border-radius: 12px;
            padding: 1rem;
        }
        
        /* Feature Cards */
        .feature-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            border: 2px solid #e9ecef;
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            border-color: #667eea;
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
        }
        
        .feature-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #343a40;
            margin-bottom: 1rem;
        }
        
        .feature-description {
            color: #6c757d;
            line-height: 1.6;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-header {
                padding: 2rem 1rem;
                text-align: center;
            }
            
            .main-header h1 {
                font-size: 2.5rem;
            }
            
            .feature-card {
                margin: 0.5rem 0;
                padding: 1.5rem;
            }
        }
        
        /* Animation Classes */
        .fade-in {
            animation: fadeIn 0.6s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .slide-in {
            animation: slideIn 0.5s ease-out;
        }
        
        @keyframes slideIn {
            from { transform: translateX(-20px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    </style>
    """