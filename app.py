import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 1. SECURITY SIDEBAR (Your Vault)
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")
if password != "Machen1923":
    st.info("Enter password to unlock.")
    st.stop()

st.sidebar.divider()
st.sidebar.title("🧠 Engine Power")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

# 2. MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("New Testament Greek for Beginners")

target_verse = st.text_input("Enter Verse (e.g., John 3:16):")

if target_verse:
    if not api_key:
        st.warning("Please enter your API Key in the sidebar to run the analysis.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
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
            st.error(f"An error occurred: {e}")
