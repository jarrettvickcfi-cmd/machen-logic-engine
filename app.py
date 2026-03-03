import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 🏛 GATE 1: THE PASSWORD
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")

if password != "Machen1923":
    st.info("Enter password to unlock the engine.")
    st.stop()  # Everything below this line is frozen until the password is correct

# 🏛 GATE 2: THE KEY (Following your logic)
# Now that they are in, we immediately grab the secret key from the basement
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("🔑 Key Error: Check your Streamlit Secrets for 'GEMINI_API_KEY'.")
    st.stop()

# 📊 TRACKING: SESSION LIMITS
if 'search_count' not in st.session_state:
    st.session_state.search_count = 50

st.sidebar.divider()
st.sidebar.metric(label="Searches Remaining", value=st.session_state.search_count)

# 🏛 MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("Professional Paid Tier | Gemini 2.5 Pro")

target_verse = st.text_input("Enter Verse (e.g., Romans 12:2):")

if target_verse and st.session_state.search_count > 0:
    try:
        # PULLING THE ENGINE
        model = genai.GenerativeModel('gemini-2.5-pro')
        
        with st.spinner("Executing 2.5 Pro Analysis..."):
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
        st.error(f"Engine Response: {e}")
