import streamlit as st
import requests

# 1. GEOFENCING (US ONLY)
def check_location():
    try:
        res = requests.get('https://ipapi.co/json/').json()
        return res.get('country_code') == 'US'
    except:
        return True 

# 2. PAGE CONFIG
st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 3. TERMS & GEOFENCE
if not check_location():
    st.error("Access Restricted: This tool is licensed for use within the United States only.")
    st.stop()

st.sidebar.title("Legal & Settings")
if not st.sidebar.checkbox("I accept the U.S. Fair Use Terms of Service"):
    st.warning("Please accept the terms in the sidebar to begin.")
    st.stop()

# 4. JOHN 1:1 LOGIC DATA
john_1_1_data = {
    "na28": "Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, καὶ θεὸς ἦν ὁ λόγος.",
    "wh": "Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, καὶ θεὸς ἦν ὁ λόγος. [No Major Variants]",
    "bridge": "Opening the Prologue: Introducing the eternal 'Logos' before creation.",
    "morphology": [
        {"Word": "ἀρχῇ", "Parsing": "Dat. Sing. Fem.", "Role": "Object of Prep (En)", "Meaning": "Beginning"},
        {"Word": "ἦν", "Parsing": "Impf. Act. Ind. 3s", "Role": "Linear/Video Action", "Meaning": "Was"},
        {"Word": "λόγος", "Parsing": "Nom. Sing. Masc.", "Role": "Subject", "Meaning": "Word"},
        {"Word": "θεόν", "Parsing": "Acc. Sing. Masc.", "Role": "Direct Object", "Meaning": "God"}
    ],
    "wooden": "In beginning was the word, and the word was toward the God, and God was the word.",
    "nuance": "The Imperfect 'ἦν' tells the believer that the Word didn't 'come into being' at the beginning; He was already there in a continuous state of existence. 'Toward the God' (πρὸς τὸν θεόν) implies an active, face-to-face relationship."
}

# 5. THE USER INTERFACE
st.title("🏛 Machen Style Greek Bible Helper")
st.write("### Verse Analysis: John 1:1")

st.markdown(f"**Greek Text (NA28 Lead):** \n## {john_1_1_data['na28']}")
st.caption(f"Westcott & Hort Reference: {john_1_1_data['wh']}")

with st.expander("Contextual Bridge"):
    st.write(john_1_1_data['bridge'])

st.write("### 📋 The Logic Map (Morphology)")
st.table(john_1_1_data['morphology'])

st.write("### 🪵 Machen Literal Translation")
st.info(john_1_1_data['wooden'])

st.write("### 🔍 Grammatical Insights")
st.write("* **Voice & Agency:** Subject is the *Logos* acting in a state of continuous being (Active Voice).")
st.write("* **Tense Priority:** The Imperfect (Linear) vs. Aorist (Punctiliar) distinction is key here.")
st.write("* **Hapax Check:** No Hapax Legomena found in this verse.")

st.success(f"**The Nuance Analysis:** \n{john_1_1_data['nuance']}")
