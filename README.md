# Dr. Home - AI-Powered Health Information Platform

![Dr. Home](https://img.shields.io/badge/Dr.%20Home-Health%20Platform-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![Perplexity AI](https://img.shields.io/badge/Powered%20by-Perplexity%20AI-purple)

## 🏥 Overview

Dr. Home is an AI-powered health information platform that provides evidence-based medical information from trusted sources. Built with Streamlit and powered by Perplexity AI, it offers a user-friendly interface for exploring symptoms, checking drug interactions, translating medical terms, and accessing health resources.

## ⚠️ Important Medical Disclaimer

**This platform is for educational purposes only and does not replace professional medical advice.**
- Always consult healthcare professionals for medical concerns
- In emergencies, call your local emergency number immediately
- This information should not be used for self-diagnosis or treatment
- Drug interactions shown are for reference only - consult your pharmacist or doctor

## ✨ Features

### 🔍 Symptom Explorer
- Get evidence-based information about symptoms from trusted medical sources
- Advanced filtering by age group, severity, and duration
- Comprehensive information including causes, red flags, and when to seek care

### 💊 Drug Interaction Checker
- Check potential interactions between medications
- Support for multiple drug combinations
- Detailed interaction analysis with severity ratings
- Clinical management recommendations

### 🏥 Medical Translator
- **Term Lookup**: Translate complex medical terms into understandable language
- **Document Translation**: Convert medical reports into patient-friendly language
- Simple definitions with pronunciation guides
- Context and related terms

### 📚 Health Resources
- Curated list of trusted medical sources (NIH, WHO, CDC, Mayo Clinic)
- Emergency contact information
- Health calculators (BMI, Heart Rate Zones)
- Links to official health resources

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Perplexity AI API key ([Get one here](https://perplexity.ai))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/dr-home.git
   cd dr-home
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```
   
   Or using the main entry point:
   ```bash
   streamlit run main.py
   ```

4. **Configure API Key:**
   - Open the application in your browser
   - Enter your Perplexity API key in the sidebar
   - Start exploring health information!

## 📁 Project Structure

```
dr-home/
├── .gitattributes              # Git configuration
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── config.py                   # Configuration settings
├── api_service.py             # Perplexity API service
├── app.py                     # Main application (legacy)
├── main.py                    # Main application entry point
├── styles.py                  # CSS styles
├── utils.py                   # Utility functions
└── pages/                     # Page modules
    ├── __init__.py           # Package initialization
    ├── symptom_explorer.py   # Symptom exploration functionality
    ├── drug_interaction.py   # Drug interaction checker
    ├── medical_translator.py # Medical term translator
    └── health_resources.py   # Health resources and calculators
```

## 🔧 Configuration

### API Configuration
The application requires a Perplexity AI API key. You can configure it through:
- The sidebar in the web interface (recommended)
- Environment variables (for deployment)

### Trusted Medical Sources
The platform queries information from trusted sources including:
- PubMed/MEDLINE articles
- NIH (National Institutes of Health)
- WHO (World Health Organization)
- CDC (Centers for Disease Control)
- Mayo Clinic
- WebMD
- Medical journals and peer-reviewed research

## 🛠️ Development

### Code Structure
The application follows a modular architecture:

- **`config.py`**: Central configuration management
- **`api_service.py`**: Perplexity API integration with specialized medical queries
- **`styles.py`**: Custom CSS styling
- **`utils.py`**: Utility functions for common tasks
- **`pages/`**: Individual page modules for different features

### Key Components

#### PerplexityService Class
```python
from api_service import PerplexityService

service = PerplexityService(api_key)
result = service.query_symptom("headache")
```

#### Styling System
Custom CSS classes for consistent UI:
- `.main-header`: Application header
- `.warning-box`: Medical disclaimers
- `.symptom-card`: Symptom information display
- `.drug-warning`: Drug interaction alerts
- `.source-citation`: Source references

## 📊 Features in Detail

### Symptom Explorer
- **Input**: Symptom description
- **Filters**: Age group, severity level, duration
- **Output**: Medical definition, causes, red flags, diagnostic approaches

### Drug Interaction Checker
- **Input**: Multiple medications
- **Analysis**: Major, moderate, and minor interactions
- **Output**: Severity ratings, mechanisms, management recommendations

### Medical Translator
- **Term Lookup**: Individual medical terms
- **Document Translation**: Full medical reports
- **Output**: Patient-friendly explanations with context

### Health Resources
- **Calculators**: BMI, Heart Rate Zones
- **Emergency Contacts**: Region-specific emergency numbers
- **Trusted Sources**: Direct links to official health resources

## 🔒 Privacy & Security

- No personal health information is stored
- API keys are handled securely through session state
- All queries are processed through Perplexity's secure API
- No data persistence beyond the current session

## 🌍 Deployment

### Local Development
```bash
streamlit run main.py
```

### Streamlit Cloud
1. Push to GitHub repository
2. Connect to Streamlit Cloud
3. Configure API key in secrets
4. Deploy automatically

### Docker (Optional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
```

## 📈 Usage Statistics

The application tracks basic usage statistics:
- Number of queries made per session
- Feature usage patterns
- No personal data collection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow Python PEP 8 style guidelines
- Add docstrings to all functions
- Include appropriate error handling
- Test with various medical scenarios
- Ensure medical accuracy and appropriate disclaimers

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚡ Performance & Limitations

### Rate Limits
- Perplexity API has rate limits based on your plan
- The application tracks query usage
- Consider implementing caching for repeated queries

### Response Time
- Typical response time: 2-5 seconds
- Depends on query complexity and API response time
- Loading indicators provide user feedback

## 🆘 Support & Troubleshooting

### Common Issues

1. **API Key Not Working**
   - Verify API key is correct
   - Check Perplexity AI account status
   - Ensure sufficient API credits

2. **Slow Response Times**
   - Normal for complex medical queries
   - Check internet connection
   - Perplexity API may have temporary delays

3. **Missing Information**
   - Try rephrasing the query
   - Use more specific medical terms
   - Check if the topic is covered by trusted sources

### Getting Help
- Check the [Issues](https://github.com/yourusername/dr-home/issues) page
- Review Perplexity AI documentation
- Contact support through GitHub issues

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Offline medical reference database
- [ ] Integration with more medical APIs
- [ ] User account system for query history
- [ ] Mobile app version
- [ ] Voice input for accessibility
- [ ] PDF report generation
- [ ] Integration with telehealth platforms

## 📞 Emergency Contacts

- **US Emergency**: 911
- **EU Emergency**: 112
- **US Poison Control**: 1-800-222-1222
- **US Mental Health Crisis**: 988

## 🙏 Acknowledgments

- **Perplexity AI** for providing the AI-powered search capabilities
- **Streamlit** for the excellent web framework
- **Medical community** for trusted health information sources
- **Open source contributors** who make projects like this possible

---

**Remember**: This tool is designed to complement, not replace, professional medical advice. Always consult with healthcare professionals for medical concerns.
