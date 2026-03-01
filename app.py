import streamlit as st
import requests

# 1. SMART GEOFENCE (US ONLY)
def check_location():
    try:
        res = requests.get('https://ipapi.co/json/', timeout=5).json()
        return res.get('country_code') == 'US'
    except:
        return True 

# 2. PAGE CONFIG
st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 3. SECURITY GATE (GEOFENCE + PASSWORD)
if not check_location():
    st.error("Access Restricted: This tool is licensed for use within the United States only.")
    st.stop()

st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter the Secret Word:", type="password")

# YOU CAN CHANGE THIS WORD TO ANYTHING YOU WANT
if password != "Machen1923":
    st.info("Please enter the password in the sidebar to unlock the Logic Engine.")
    st.stop()

if not st.sidebar.checkbox("I accept the U.S. Fair Use Terms of Service"):
    st.warning("Please accept the terms to reveal the analysis.")
    st.stop()

# 4. DATA ENGINE
john_1_1_data = {
    "na28": "Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, καὶ θεὸς ἦν ὁ λόγος.",
    "morphology": [
        {"Word": "ἀρχῇ", "Parsing": "Dat. Sing. Fem.", "Role": "Object of Prep (En)", "Meaning": "Beginning"},
        {"Word": "ἦν", "Parsing": "Impf. Act. Ind. 3s", "Role": "Linear/Video Action", "Meaning": "Was"},
        {"Word": "λόγος", "Parsing": "Nom. Sing. Masc.", "Role": "Subject", "Meaning": "Word"},
        {"Word": "θεόν", "Parsing": "Acc. Sing. Masc.", "Role": "Direct Object", "Meaning": "God"}
    ],
    "wooden": "In beginning was the word, and the word was toward the God, and God was the word.",
    "nuance": "The Imperfect 'ἦν' identifies eternal, continuous existence. The Word didn't 'start' at the beginning; He was already there."
}

# 5. DISPLAY
st.title("🏛 Machen Style Greek Bible Helper")
st.markdown(f"**John 1:1 Analysis:** \n## {john_1_1_data['na28']}")
st.table(john_1_1_data['morphology'])
st.info(f"**Literal Translation:** {john_1_1_data['wooden']}")
st.success(f"**Theological Nuance:** {john_1_1_data['nuance']}")
