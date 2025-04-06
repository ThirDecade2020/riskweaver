import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from country_inquiry_store import record_country_inquiry

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Enhanced custom CSS with a stronger green/gold gradient and bolder styling
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

/* 
   Stronger gradient:
   - Starts at a deep green (#013220)
   - Transitions to a mid-green (#025832)
   - Ends in bold gold (#FFD700)
*/
body {
    background: linear-gradient(135deg, #013220 0%, #025832 50%, #FFD700 100%);
    color: #FFD700;
    font-family: 'Press Start 2P', monospace;
    image-rendering: pixelated;
    margin: 0;
    padding: 0;
}

/* 
   Bolder text shadow for headers:
   - Larger glow effect to make them pop against the gradient 
*/
h1, h2, h3 {
    color: #FFD700;
    text-shadow: 3px 3px 8px rgba(255, 215, 0, 0.8);
}

/* 
   Animated glowing effect for buttons:
   - Thicker glow 
   - Slightly longer animation cycle 
*/
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

/* 
   Bold label for text input 
*/
div.stTextInput > label {
    font-weight: bold;
    text-shadow: 1px 1px 3px rgba(255, 215, 0, 0.8);
}

/* Add some padding for the main content area */
.css-1lcbmhc, .css-18e3th9, .css-1outpf7 {
    padding: 1rem !important;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# App title and input field
st.title("RiskWeaver – Cybersecurity Risk Analyzer")
country = st.text_input("Enter a country name:")

# Define a function to get cybersecurity risks from OpenAI using GPT-4,
# including up-to-date sources and a one-paragraph insight.
def get_cybersecurity_risks(country):
    prompt = (
        f"Using the most recent publicly available data as of now, and based on information from {country}'s official "
        f"government cybersecurity agency and other reputable sources, list the top 5 cybersecurity risks for {country}. "
        f"Additionally, provide a one-paragraph insight that discusses any similarities, glaring differences, or shared patterns "
        f"among these risks. Include specific references (e.g., agency names, website links, and publication years) without speculating."
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

# When the button is clicked, record the inquiry and fetch the risks
if st.button("Analyze Risks"):
    if country.strip():
        record_country_inquiry(country)
        st.success(f"Running analysis for {country}...")
        with st.spinner("Fetching cybersecurity risks..."):
            risks = get_cybersecurity_risks(country)
            st.write(risks)
    else:
        st.error("Please enter a valid country name.")

