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
# with a prompt that instructs the model to use up-to-date sources and include publication years.
def get_cybersecurity_risks(country):
    prompt = (
        f"Using the most recent publicly available data as of now, and based on information from {country}'s official "
        f"government cybersecurity agency and other reputable sources, list the top 5 cybersecurity risks for {country}. "
        f"Additionally, provide a one-paragraph insight that discusses any similarities, glaring differences, or shared patterns "
        f"among these risks. Include specific references such as the agency's name, website links, and the publication year of the data. "
        f"Do not speculate beyond publicly available data."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Using GPT-4 for in-depth, current analysis
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
        # Record the inquiry in our persistence layer (stored in the JSON file)
        record_country_inquiry(country)
        st.success(f"Running analysis for {country}...")
        with st.spinner("Fetching cybersecurity risks..."):
            risks = get_cybersecurity_risks(country)
            st.write(risks)
    else:
        st.error("Please enter a valid country name.")

