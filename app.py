import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 1. SECURITY SIDEBAR (Gatekeeper)
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")
if password != "Machen1923":
    st.info("Enter password to unlock.")
    st.stop()

# 2. ENGINE INITIALIZATION (The Jarrett Method)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 3. MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("New Testament Greek for Beginners")

target_verse = st.text_input("Enter Verse (e.g., John 3:16):")

if target_verse:
    try:
        # Using your confirmed engine
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
        
        response = model.generate_content(prompt)
        st.markdown(response.text)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
