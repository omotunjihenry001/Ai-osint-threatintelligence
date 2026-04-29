
AI-Powered OSINT Threat Intelligence System

Overview
This project implements an AI-driven Open Source Intelligence (OSINT) system designed to automate cyber threat monitoring and risk assessment.

It combines Natural Language Processing (NLP) with rule-based intelligence to identify, classify, and prioritise cyber threats from publicly available data sources.


Features
- OSINT data collection (news & cyber threat feeds)
- Data preprocessing and text cleaning
- Machine learning classification model (threat detection)
- Hybrid risk scoring system (ML + keyword intelligence)
- Streamlit dashboard for real-time threat monitoring

Methodology

The system uses a hybrid approach:

- **ML Model** → predicts likelihood of cyber threat  
- **Rule-based engine** → identifies critical keywords (e.g. ransomware, breach)  
- **Final Score** → weighted combination for robust decision-making  


Example Output

| Text | Risk Level | Score |
|------|-----------|------|
| Cyber-attacks surge globally | High | 0.72 |
| Malware detected in systems | Medium | 0.55 |
| Tech news update | Low | 0.04 |


Dashboard

The system includes a Streamlit dashboard for:

- Threat monitoring  
- Risk filtering  
- Top risk identification  


Installation

```bash
pip install -r requirements.txt
streamlit run app.py

![Dashboard](screenshots/dashboard.png)
