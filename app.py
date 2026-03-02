import streamlit as st
import requests

# --- 1. CONFIGURATION & GEOFENCING ---
st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

def is_user_in_usa():
    try:
        response = requests.get('https://ipapi.co/country/', timeout=5)
        return response.text.strip() == "US"
    except:
        # Fallback to True if API is down to avoid locking you out, 
        # but in production, you'd handle this more strictly.
        return True

if not is_user_in_usa():
    st.error("Access Restricted: This application is only available within the United States.")
    st.stop()

# --- 2. SECURITY GATE ---
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")

if password != "Machen1923":
    st.sidebar.warning("Please enter the correct password to proceed.")
    st.title("🏛 Machen Logic Engine")
    st.info("Welcome, Student. Please authenticate via the sidebar to begin your Greek studies.")
    st.stop()

# --- 3. APP INTERFACE ---
st.title("🏛 Machen Scholar Assistant")
st.markdown("### *New Testament Greek for Beginners*")

target_verse = st.text_input("Enter Verse (e.g., John 1:1, Romans 8:1):", placeholder="e.g., John 3:16")
show_phonetic = st.checkbox("Provide Phonetic Erasmian Guide")

if target_verse:
    st.divider()
    
    # In a full-scale app, we would call a Greek API here (like StepBible or Python-Greek-Utils)
    # For this logic engine, we are setting up the pedagogical structure:
    
    st.subheader("📜 The Greek Text (Majority Text)")
    st.write(f"*Displaying Majority Text for {target_verse}...*")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Westcott & Hort**")
        st.caption("Primary textual basis.")
    with col2:
        st.markdown("**Nestle Comparison**")
        st.caption("Variant readings noted.")

    if show_phonetic:
        st.subheader("🗣 Phonetic Guide (Erasmian)")
        st.info("Phonetic breakdown would appear here.")

    st.subheader("📊 Morphology Table")
    st.markdown("""
    | Word | Case/Number/Gender | Tense/Voice/Mood | Machen Definition |
    | :--- | :--- | :--- | :--- |
    | *Example* | Nom. Sing. Masc. | N/A | The word |
    """)

    st.subheader("🪵 Machen Literal Translation")
    st.markdown(f"> *'Wooden' rendering of {target_verse} following strict inflectional values...*")

    st.subheader("💡 Grammatical Insights")
    st.bullet_point("Aorist vs. Present: Identifying punctiliar vs. linear action.")
    st.bullet_point("Article Function: Analysis of the presence or absence of 'ho'.")
    st.bullet_point("Hapax Check: Checking for words appearing only once in the GNT.")

    st.divider()
    st.subheader("🗣 Plain Conversation")
    st.write("Here we explain the 'So What?'—how the Greek nuances change our understanding for today.")

# --- 4. SIDEBAR FOOTER ---
st.sidebar.divider()
st.sidebar.info("System: Machen Logic Engine v1.0\nTextual Basis: Westcott & Hort")
