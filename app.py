import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 1. SECURITY SIDEBAR
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")
if password != "Machen1923":
    st.info("Enter password to unlock.")
    st.stop()

# 2. USAGE TRACKER (Per-Session)
if 'search_count' not in st.session_state:
    st.session_state.search_count = 50

st.sidebar.divider()
st.sidebar.title("📊 Session Usage")
st.sidebar.metric(label="Searches Remaining", value=st.session_state.search_count)

if st.session_state.search_count <= 0:
    st.error("Session limit reached. Please refresh to continue.")
    st.stop()

# 3. MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("Professional Paid Tier | Majority Text Analysis")

target_verse = st.text_input("Enter Verse (e.g., Ephesians 2:8):")

if target_verse:
    try:
        # Pulls your hidden key from Streamlit Secrets
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # PRO model provides higher stability and better Greek morphology
        model = genai.GenerativeModel('gemini-2.5-pro')
        
        with st.spinner("Consulting the Majority Text..."):
            # A 2-second 'politeness' delay to protect your Paid Tier quota
            time.sleep(2) 
            
            prompt = f"""
            You are a Koine Greek scholar following J. Gresham Machen's methods.
            Analyze {target_verse} with these rules:
            1. Use Majority Text (Byzantine).
            2. Compare with Westcott & Hort and Nestle readings.
            3. Provide full Morphology (Case, Number, Gender / Tense, Voice, Mood).
            4. Identify any Hapax Legomenon.
            5. Provide a "Machen Literal Translation" (wooden but accurate).
            6. Explain Aorist vs Present actions.
            7. End with 'Plain Conversation' explaining the meaning today.
            """
            
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.search_count -= 1
            
    except Exception as e:
        if "429" in str(e):
            st.error("The engine is busy. Please wait 30 seconds and try again.")
        else:
            st.error(f"Engine Error: {e}")
