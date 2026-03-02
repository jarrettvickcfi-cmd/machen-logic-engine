import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# --- 2. GEOFENCE (Bypassed for Streamlit Cloud stability) ---
def is_user_in_usa():
    return True 

if not is_user_in_usa():
    st.error("Access Restricted.")
    st.stop()

# --- 3. SECURITY & API KEY ---
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")

if password != "Machen1923":
    st.sidebar.warning("Please enter the correct password to proceed.")
    st.stop()

st.sidebar.divider()
st.sidebar.subheader("🧠 Engine Power")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

# --- 4. APP INTERFACE ---
st.title("🏛 Machen Scholar Assistant")
st.markdown("### *New Testament Greek for Beginners*")

target_verse = st.text_input("Enter Verse (e.g., John 1:1, Romans 8:1):", placeholder="e.g., John 3:16")

if target_verse:
    if not api_key:
        st.warning("⚠️ Please enter your API Key in the sidebar to generate the analysis.")
    else:
        st.markdown(f"### Analysis for: {target_verse}")
        with st.spinner("Consulting the Greek texts..."):
            try:
                genai.configure(api_key=api_key)
                # Using the standard Gemini model
               model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                prompt = f"""
                You are a Koine Greek scholar and pedagogical assistant using J. Gresham Machen's methods.
                Analyze the following verse: {target_verse}
                
                Format EXACTLY like this:
                ## 📜 The Greek Text
                (Provide Majority Text)
                
                ## 📝 Textual Notes
                * **Westcott & Hort:** (Notes here)
                * **Nestle Comparison:** (Notes here)
                
                ## 📊 Morphology Table
                (Markdown table with Case/Number/Gender for nouns/adj, Tense/Voice/Mood/Person/Number for verbs)
                
                ## 🪵 Machen Literal Translation
                (Wooden translation maintaining Greek word order)
                
                ## 💡 Grammatical Insights
                * Explain Aorist vs Present if applicable.
                * Explain Article function if applicable.
                * Mention if there is a Hapax Legomenon.
                
                ## 🗣 Plain Conversation
                (Explain the meaning in modern English and the 'So What?')
                """
                
                response = model.generate_content(prompt)
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.sidebar.divider()
st.sidebar.info("System: Machen Logic Engine v2.0")
