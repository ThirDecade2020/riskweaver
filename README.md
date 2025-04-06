RiskWeaver – Cybersecurity Risk Analyzer

RiskWeaver is a Python-based web application built with Streamlit that provides an in-depth cybersecurity risk analysis for a given country. The app leverages GPT-4 via the OpenAI API to list the top 5 cybersecurity risks based on publicly available data from the country's official cybersecurity agency and other reputable sources. It also offers a one-paragraph insight discussing similarities, differences, and shared patterns among these risks. Additionally, a sidebar presents a curated list of secondary sources for further investigation.

Features:

Modern, Eye-Catching UI: A bold green/gold theme with a pixelated retro aesthetic, including animated glowing buttons and dynamic gradient backgrounds.
Interactive Cybersecurity Analysis: Users enter a country name to fetch a detailed analysis that includes the top 5 risks and a concise insight with proper citations (including publication years and references to official agencies).
Persistence: Tracks each inquiry by storing the count in a JSON file (country_inquiry_data.json), allowing you to see which countries have been queried.
Secondary Sources Sidebar: Displays a list of publicly available secondary sources (such as news reports and cybersecurity blogs) for further investigation.
Installation: Prerequisites:

Python 3.8+ (this project has been developed using Python 3.13)
Pip (Python package installer)
Setup Instructions:

Clone the repository: git clone https://github.com/ThirDecade2020/riskweaver.git cd riskweaver
Create and activate a virtual environment: python3 -m venv venv source venv/bin/activate
Install the required packages: pip install -r requirements.txt
Set up your environment variables: Create a file named .env in the project’s root directory and add: OPENAI_API_KEY=your_actual_api_key_here
Usage:

Run the application (with your virtual environment activated): streamlit run riskweaver_app.py
Interact with the app:
Enter a country name in the provided text field.
Click the "Analyze Risks" button.
The app will display the top 5 cybersecurity risks, a one-paragraph insight with proper citations, and a sidebar with secondary sources for further investigation.
Project Structure: riskweaver/ riskweaver_app.py - Main Streamlit application (UI, API integration, and persistence) country_inquiry_store.py - Module for tracking inquiry counts in a JSON file country_inquiry_data.json - JSON file serving as a simple database for inquiry counts .env - Environment file for storing API keys (not committed) .gitignore - Git ignore file (excludes .env, pycache, and the JSON data file) requirements.txt - List of required Python packages README.md - This README file tests/ - Directory containing test scripts (e.g., test_openai.py)

Contributing: Contributions are welcome! Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

License: This project is licensed under the Apache-2.0 License.

Acknowledgements:

Streamlit for its intuitive UI framework.
OpenAI for providing GPT-4 and the powerful API.
The cybersecurity community and open source projects that supply publicly available data on cyber risks.
