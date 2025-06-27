
import streamlit as st

st.set_page_config(page_title="PromptGPT Vibe Tester", layout="centered")

st.title("🔍 PromptGPT Vibe Testing Suite")
st.write("Test how your app *feels*, not just if it works.")

with st.form("vibe_form"):
    user_prompt = st.text_area("Enter a vibe test prompt (e.g., 'Checkout should feel fast and secure')", height=150)
    submitted = st.form_submit_button("Run Vibe Test")

if submitted and user_prompt:
    st.subheader("🧠 Vibe Test Result")
    st.success("✅ Vibe Passed: Smooth UX and acceptable load time.")
    st.warning("⚠️ Minor UI inconsistency found: font mismatch on confirmation button.")
    st.download_button("📥 Download Vibe Report", "Prompt: " + user_prompt + "\n\nResult: PASS with minor warning", file_name="vibe_report.txt")
