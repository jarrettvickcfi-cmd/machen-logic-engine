import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 1. SECURITY SIDEBAR
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")
if password != "Machen1923":
    st.info("Enter password to unlock.")
    st.stop()

# 2. MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("Professional Paid Tier | Gemini 2.5 Pro")

target_verse = st.text_input("Enter Verse (e.g., Ephesians 2:8):")

if target_verse:
    try:
        # We are using st.secrets.get to ensure it pulls correctly from the dashboard
        key = st.secrets.get("GEMINI_API_KEY")
        
        if not key:
            st.error("🔑 Key Not Found: Go to Streamlit Settings > Secrets and add your GEMINI_API_KEY.")
            st.stop()
            
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-2.5-pro')
        
        with st.spinner("Consulting 2.5 Pro..."):
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
            
    except Exception as e:
        st.error(f"Engine Error: {e}")
