import streamlit as st
import google.generativeai as genai
import requests

st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

# 1. THE SMART GEOFENCE (Client IP Intercept)
def check_client_location():
    try:
        # Intercept the connection headers to find the user's real IP
        headers = st.context.headers
        client_ip = headers.get("X-Forwarded-For", "")
        
        if client_ip:
            # If routed through multiple servers, the real user is the first IP in the list
            client_ip = client_ip.split(",")[0].strip()
            
            # Check the USER'S location, not Streamlit's server location
            res = requests.get(f'https://ipapi.co/{client_ip}/json/', timeout=5).json()
            return res.get('country_code') == 'US'
            
        # If no IP header is found, default to safe so you don't get locked out
        return True
    except:
        return True

# Trigger the fence
if not check_client_location():
    st.error("🛑 Access Restricted: This tool is licensed for use within the United States only.")
    st.stop()

# 2. SECURITY SIDEBAR (Your Vault)
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")
if password != "Machen1923":
    st.info("Enter password to unlock.")
    st.stop()

st.sidebar.divider()
st.sidebar.title("🧠 Engine Power")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

# 3. MAIN INTERFACE
st.title("🏛 Machen Scholar Assistant")
st.caption("New Testament Greek for Beginners")

target_verse = st.text_input("Enter Verse (e.g., John 3:16):")

if target_verse:
    if not api_key:
        st.warning("Please enter your API Key in the sidebar to run the analysis.")
    else:
        try:
            genai.configure(api_key=api_key)
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
