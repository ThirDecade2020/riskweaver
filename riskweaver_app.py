import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from country_inquiry_store import record_country_inquiry

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Enhanced custom CSS for a bold green/gold theme with retro styling
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

body {
    background: linear-gradient(135deg, #013220 0%, #025832 50%, #FFD700 100%);
    color: #FFD700;
    font-family: 'Press Start 2P', monospace;
    image-rendering: pixelated;
    margin: 0;
    padding: 0;
}

h1, h2, h3 {
    color: #FFD700;
    text-shadow: 3px 3px 8px rgba(255, 215, 0, 0.8);
}

@keyframes glow {
    0% { box-shadow: 0 0 10px #FFD700; }
    50% { box-shadow: 0 0 30px #FFD700; }
    100% { box-shadow: 0 0 10px #FFD700; }
}

div.stButton > button {
    background-color: #FFD700;
    color: #013220;
    border: 2px solid #FFD700;
    border-radius: 8px;
    font-weight: bold;
    animation: glow 1.8s ease-in-out infinite;
    cursor: pointer;
}

div.stTextInput > label {
    font-weight: bold;
    text-shadow: 1px 1px 3px rgba(255, 215, 0, 0.8);
}

/* Sidebar styling */
div[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #013220, #025832);
    color: #FFD700;
    font-family: 'Press Start 2P', monospace;
}

.css-1lcbmhc, .css-18e3th9, .css-1outpf7 {
    padding: 1rem !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# App title and main input field
st.title("RiskWeaver – Cybersecurity Risk Analyzer")
country = st.text_input("Enter a country name:")

# Sidebar: Secondary sources for further investigation
st.sidebar.markdown("### Secondary Sources")
st.sidebar.markdown("""
- [Krebs on Security](https://krebsonsecurity.com/)
- [The Hacker News](https://thehackernews.com/)
- [Threatpost](https://threatpost.com/)
- [SecurityWeek](https://www.securityweek.com/)
- [CyberScoop](https://www.cyberscoop.com/)
""")

# Function to get cybersecurity risks from GPT-4 with up-to-date sources and insights
def get_cybersecurity_risks(country):
    prompt = (
        f"Using the most recent publicly available data, and based on information from {country}'s official "
        f"government cybersecurity agency and reputable sources, list the top 5 cybersecurity risks for {country}. "
        f"Additionally, provide a one-paragraph insight that discusses any similarities, differences, or shared patterns "
        f"among these risks. Include specific references (agency names, website links, publication years) without speculating."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity risk analyst who provides up-to-date, factual information with proper citations including publication years."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# On button click, record inquiry and fetch risks
if st.button("Analyze Risks"):
    if country.strip():
        record_country_inquiry(country)
        st.success(f"Running analysis for {country}...")
        with st.spinner("Fetching cybersecurity risks..."):
            risks = get_cybersecurity_risks(country)
            st.write(risks)
    else:
        st.error("Please enter a valid country name.")

# Footer: Fixed at the bottom of the page with a hyperlink to Sundai.Club
footer_html = """
<div style="
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #013220;
    color: #FFD700;
    text-align: center;
    padding: 10px 0;
    font-family: 'Press Start 2P', monospace;
">
  <a href="https://www.sundai.club/projects/8a816790-74e5-4460-a9c0-2d2ba8ec6832" target="_blank" style="
    color: #FFD700;
    text-decoration: none;
    font-size: 14px;
  ">Built at Sundai.Club</a>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

