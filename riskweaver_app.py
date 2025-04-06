import streamlit as st

# Inject custom CSS for a pixelated design with green and gold
custom_css = """
<style>
/* Set the background to dark green and text to gold, with a pixelated effect */
body {
    background-color: #013220;
    color: #FFD700;
    font-family: 'Courier New', monospace;
    image-rendering: pixelated;
}

/* Style header elements in gold */
h1, h2, h3 {
    color: #FFD700;
}

/* Style the Analyze Risks button */
div.stButton > button {
    background-color: #FFD700;
    color: #013220;
    border: none;
    font-weight: bold;
}

/* Style text input labels to be bold */
div.stTextInput > label {
    font-weight: bold;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# App title
st.title("RiskWeaver – Cybersecurity Risk Analyzer")

# Input: Enter a country name
country = st.text_input("Enter a country name:")

# Button to trigger risk analysis
if st.button("Analyze Risks"):
    if country.strip():
        st.success(f"Running analysis for {country}...")
    else:
        st.error("Please enter a valid country name.")

