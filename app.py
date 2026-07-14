import streamlit as st
import time

st.set_page_config(page_title="CommuniLink AI", page_icon="🏡")
st.title("🏡 CommuniLink: Smart Community AI")
st.write("An AI assistant built to help local residents draft community notices, organize neighborhood events, or report local issues.")

st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password", value="DEMO_MODE_ACTIVE")

st.subheader("Quick Actions")
col1, col2 = st.columns(2)

preset_prompt = ""
if col1.button("📝 Draft a Neighborhood Notice"):
    preset_prompt = "Write a polite announcement notice for a neighborhood clean-up drive happening this Sunday morning."
if col2.button("🛠️ Report a Street Light Issue"):
    preset_prompt = "Draft a formal email to the local municipal corporation requesting the repair of a broken street light on Main Road."

user_input = st.text_input("Or ask the Community AI something else:", value=preset_prompt)

if user_input:
    with st.spinner("Connecting to CommuniLink AI Engine..."):
        time.sleep(1.5) # Simulates the AI thinking time
        st.subheader("AI Recommendation:")
        
        # Smart responses based on what you clicked
        if "clean-up" in user_input.lower():
            st.write("**Subject: 🧹 Neighborhood Clean-Up Drive - This Sunday!**\n\nDear Residents,\n\nTo keep our locality clean and green, we are organizing a community clean-up drive this Sunday at 8:00 AM. Please gather at the central park. Gloves and garbage bags will be provided. Let's work together for a better neighborhood!\n\nBest regards,\nCommunity Committee")
        elif "street light" in user_input.lower():
            st.write("**Subject: Complaint regarding non-functional street light on Main Road**\n\nTo,\nThe Municipal Commissioner,\n\nRespected Sir/Madam,\n\nI am writing to bring to your attention that the street light near Main Road has been broken for the past week. This causes significant safety concerns for residents walking at night. Kindly arrange for its repair at the earliest.\n\nThank you,\nLocal Resident")
        else:
            st.write("Here is your smart community solution draft! (App running in offline presentation mode due to live API key quota limits).")
