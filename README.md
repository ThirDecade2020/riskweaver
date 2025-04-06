RiskWeaver – Cybersecurity Risk Analyzer

RiskWeaver is a Python-based web application built with Streamlit that provides an in-depth cybersecurity risk analysis for a given country. The app leverages GPT-4 via the OpenAI API to list the top 5 cybersecurity risks based on publicly available data from the country’s official cybersecurity agency and other reputable sources. It also includes a one-paragraph insight discussing similarities, differences, and shared patterns among these risks. Additionally, a sidebar lists secondary sources for further investigation.

Features

• Modern, Eye-Catching UI:
  - Bold green/gold retro theme with pixelated fonts
  - Animated glowing buttons and a striking gradient background

• Interactive Cybersecurity Analysis:
  - Enter a country name to fetch a detailed GPT-4 analysis
    • Top 5 cybersecurity risks
    • A one-paragraph insight with references, publication years, and official agency names

• Persistence (JSON-based):
  - Tracks each inquiry by storing query counts in a JSON file (country_inquiry_data.json)

• Secondary Sources Sidebar:
  - Provides clickable links to publicly available resources (news sites, security blogs, etc.) for further investigation

Prerequisites

• Python 3.8+ (this project is developed using Python 3.13)
• Pip (Python package installer)

Setup Instructions

Clone the Repository:
  git clone https://github.com/ThirDecade2020/riskweaver.git
  cd riskweaver
Create and Activate a Virtual Environment:
  python3 -m venv venv
  source venv/bin/activate
Install Required Packages:
  pip install -r requirements.txt
Set Up Environment Variables:
  Create a file named .env in the project’s root directory and add:
  OPENAI_API_KEY=your_actual_api_key_here
Usage

Run the Application:
  With your virtual environment activated, run:
  streamlit run riskweaver_app.py
Interact with the App:
  - Enter a country name in the provided text field.
  - Click Analyze Risks to fetch the analysis.
  - View the top 5 cybersecurity risks and a detailed one-paragraph insight with proper citations.
  - Consult the Secondary Sources sidebar for additional reading.
Project Structure

riskweaver/
  • riskweaver_app.py  - Main Streamlit app (UI, OpenAI integration, persistence)
  • country_inquiry_store.py  - Module for storing query counts in JSON
  • country_inquiry_data.json  - JSON file tracking the number of queries per country
  • .env  - Environment variables (API key, etc.) [not committed]
  • .gitignore  - Excludes .env, __pycache__, .DS_Store, etc.
  • requirements.txt  - Python dependencies
  • README.md  - This file
  • tests/  - Directory containing test scripts (e.g., test_openai.py)

Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with enhancements or bug fixes.

License

This project is licensed under the Apache-2.0 License.

Acknowledgements

• Streamlit – for its intuitive UI framework
• OpenAI – for providing GPT-4 and the powerful API
• The cybersecurity community and open source projects that supply publicly available data on cyber risks
