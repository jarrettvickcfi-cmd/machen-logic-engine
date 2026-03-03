import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 1. SECURITY SIDEBAR (Password Only)
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")
if password != "Machen1923":
    st.info("Enter password to unlock.")
    st.stop()

# 2. SEARCH COUNTER (Per-Session)
if 'search_count' not in st.session_state:
    st.session_state.search_count = 50

st.sidebar.divider()
st.sidebar.title("📊 Usage")
st.sidebar.metric(label="Searches Remaining", value=st.session_state.search_count)

if st.session_state.search_count <= 0:
    st.error("Session limit reached. Please refresh to continue.")
    st.stop()

# 3. MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("New Testament Greek for Beginners")

target_verse = st.text_input("Enter Verse (e.g., John 3:16):")

if target_verse:
    try:
        # Pulls your hidden key from the Streamlit "Basement" (Secrets)
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Using the engine your research discovered works
        model = genai.GenerativeModel('gemini-2.5-flash')
        
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
        
        with st.spinner("Consulting Majority Text..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.search_count -= 1
            
    except Exception as e:
        st.error(f"Engine Error. Ensure 'GEMINI_API_KEY' is in your Streamlit Secrets! {e}")
