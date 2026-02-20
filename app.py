

import streamlit as st
import ollama

st.title("Professional Email Reply Generator")

st.markdown("""
This app uses the gemma3:4b model via Ollama to generate professional email replies. Fill in the required fields and settings, then click Generate.
""")

# Sidebar settings
with st.sidebar:
    st.header("Settings")
    ollama_url = st.text_input("Ollama URL", value="http://127.0.0.1:11434")
    model_name = st.text_input("Model name", value="gemma3:4b")
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
    max_tokens = st.slider("Max tokens", min_value=64, max_value=2048, value=512, step=32)

# Main UI
incoming_email = st.text_area("Email you received")
desired_goal = st.text_area("What do you want to achieve?")
user_name = st.text_input("Your name (optional)")
user_email = st.text_input("Your email")

# Tone selectbox
tone = st.selectbox(
    "Tone",
    ["Formal", "Friendly", "Short", "Customer Support", "Follow-up"]
)

reply = ""

if st.button("Generate"):
    if incoming_email and desired_goal and user_email:
        # Tone instructions
        tone_instructions = {
            "Formal": "Write the reply in a formal, professional tone. Use proper grammar and complete sentences.",
            "Friendly": "Write the reply in a friendly, approachable tone. Be warm and personable.",
            "Short": "Write a concise and brief reply. Keep it as short as possible while being clear.",
            "Customer Support": "Write the reply as a customer support agent. Be helpful, empathetic, and solution-oriented.",
            "Follow-up": "Write the reply as a follow-up message. Reference the previous conversation and encourage a response."
        }
        prompt = (
            f"You are a professional assistant. {tone_instructions[tone]}\n"
            f"Incoming email:\n{incoming_email}\n"
            f"Goal:\n{desired_goal}\n"
            f"Your name: {user_name if user_name else '[Not provided]'}\n"
            f"Your email: {user_email}\n"
            "Reply:"
        )
        try:
            response = ollama.generate(
                model=model_name,
                prompt=prompt,
                options={"temperature": temperature, "num_predict": max_tokens}
            )
            reply = response['response']
            st.success("Generated Reply:")
            st.write(reply)
        except Exception as e:
            st.error(f"Error generating reply: {e}")
    else:
        st.warning("Please fill in all required fields (email you received, what you want to achieve, your email).")

# Download button
if reply:
    st.download_button(
        label="Download Reply as .txt",
        data=reply,
        file_name="email_reply.txt",
        mime="text/plain"
    )
