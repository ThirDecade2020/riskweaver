import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from country_inquiry_store import record_country_inquiry

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Inject custom CSS for a pixelated design with green and gold
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
body {
    background-color: #013220;
    color: #FFD700;
    font-family: 'Press Start 2P', monospace;
    image-rendering: pixelated;
}
h1, h2, h3 {
    color: #FFD700;
}
div.stButton > button {
    background-color: #FFD700;
    color: #013220;
    border: none;
    font-weight: bold;
}
div.stTextInput > label {
    font-weight: bold;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# App title and input field
st.title("RiskWeaver – Cybersecurity Risk Analyzer")
country = st.text_input("Enter a country name:")

# Define a function to get cybersecurity risks from OpenAI using GPT-4,
# and provide a one-paragraph insight on similarities, differences, or shared patterns.
def get_cybersecurity_risks(country):
    prompt = (
        f"Based on publicly available data from {country}'s official government cybersecurity agency "
        f"and other reputable sources, list the top 5 cybersecurity risks for {country}. "
        "Additionally, provide a one-paragraph insight discussing any similarities, glaring differences, or shared patterns among these risks. "
        "Include specific references to the agency's name or website where possible, and do not speculate beyond publicly available data. "
        "Provide sources or links where appropriate."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Using GPT-4 for in-depth analysis
            messages=[
                {"role": "system", "content": "You are a cybersecurity risk analyst, providing factual information with proper citations."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# When the button is clicked, record the inquiry and fetch the risks
if st.button("Analyze Risks"):
    if country.strip():
        # Record the inquiry in our persistence layer (stored in the JSON file)
        record_country_inquiry(country)
        st.success(f"Running analysis for {country}...")
        with st.spinner("Fetching cybersecurity risks..."):
            risks = get_cybersecurity_risks(country)
            st.write(risks)
    else:
        st.error("Please enter a valid country name.")

