import streamlit as st
from country_inquiry_store import record_country_inquiry

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

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# App title
st.title("RiskWeaver – Cybersecurity Risk Analyzer")

# Input: Country name
country = st.text_input("Enter a country name:")

# Button to trigger risk analysis and record inquiry
if st.button("Analyze Risks"):
    if country.strip():
        # Record the inquiry for persistence (data is stored in the JSON file)
        record_country_inquiry(country)
        st.success(f"Running analysis for {country}...")
    else:
        st.error("Please enter a valid country name.")

