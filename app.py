import streamlit as st
import requests
import google.generativeai as genai

# --- 1. CONFIGURATION & GEOFENCING ---
st.set_page_config(page_title="Machen Logic Engine", page_icon="📖")

def is_user_in_usa():
    try:
        response = requests.get('https://ipapi.co/country/', timeout=5)
        return response.text.strip() == "US"
    except:
        return True

if not is_user_in_usa():
    st.error("Access Restricted: This application is only available within the United States.")
    st.stop()

# --- 2. SECURITY GATE ---
st.sidebar.title("🔐 Secure Access")
password = st.sidebar.text_input("Enter Secret Word:", type="password")

if password != "Machen1923":
    st.sidebar.warning("Please enter the correct password to proceed.")
    st.stop()

# --- 3. AI ENGINE SETUP ---
st.sidebar.divider()
st.sidebar.subheader("⚙️ Engine Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-pro')

# --- 4. APP INTERFACE ---
st.title("🏛 Machen Scholar Assistant")
st.markdown("### *New Testament Greek for Beginners*")

target_verse = st.text_input("Enter Verse (e.g., John 1:1, Romans 8:1):", placeholder="e.g., John 3:16")
show_phonetic = st.checkbox("Provide Phonetic Erasmian Guide")

# The strict Machen instructions for the AI
machen_instructions = f"""
You are a Koine Greek scholar and pedagogical assistant specializing in the methods of J. Gresham Machen.
Your primary goal is to help the user master the Greek New Testament using a formal, inflection-based approach.

Analyze the following verse: {target_verse}

Follow these rules STRICTLY and format your response with Markdown:
1. **The Greek Text**: Provide the Majority Text.
2. **Textual Notes**: Provide Westcott & Hort (labeled "Westcott") and Nestle comparison (labeled "Nestle").
3. **Phonetic Guide**: Only include an Erasmian phonetic guide if this is true: {show_phonetic}.
4. **Morphology Table**: Create a markdown table for key words identifying Case/Number/Gender for nouns/adjectives/participles, and Tense/Voice/Mood/Person/Number for verbs.
5. **Machen Literal Translation**: Provide a literal translation using Machen's vocabulary definitions strictly, maintaining Greek word order where possible.
6. **Grammatical Insights**: 3-4 bullet points. You MUST explain Aorist (punctiliar) vs Present (linear) action if applicable. You MUST explain the function of the Article if applicable. You MUST mention if a word is a 'Hapax Legomenon'.
7. **Plain Conversation**: Provide a separate section titled "Plain Conversation" explaining the verse's meaning in modern English, focusing on how the Greek nuances change our understanding today.
"""

if target_verse:
    if not api_key:
        st.warning("⚠️ Please enter your API Key in the sidebar to generate the analysis.")
    else:
        st.divider()
        with st.spinner(f"Consulting the texts for {target_verse}..."):
            try:
                # Ask the AI to generate the response based on our rules
                response = model.generate_content(machen_instructions)
                
                # Display the AI's response
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- 5. SIDEBAR FOOTER ---
st.sidebar.divider()
st.sidebar.info("System: Machen Logic Engine v2.0\nPowered by Gemini")
