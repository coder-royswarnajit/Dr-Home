# styles.py
"""CSS styles for Dr. Home application"""

def get_custom_css():
    """Returns custom CSS for the application"""
    return """
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
        
        .metric-card {
            background-color: #f0f8ff;
            border: 1px solid #4CAF50;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
            text-align: center;
        }
        
        .emergency-card {
            background-color: #ffebee;
            border: 2px solid #f44336;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
        }
    </style>
    """