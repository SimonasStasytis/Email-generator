
import streamlit as st
import ollama

st.title("Professional Email Reply Generator")

st.markdown("""
This app uses the gemma3:4b model via Ollama to generate professional email replies. Enter the incoming email and your desired goal for the reply.
""")

incoming_email = st.text_area("Paste the incoming email:")
desired_goal = st.text_input("Desired goal for the reply:")

if st.button("Generate Reply"):
    if incoming_email and desired_goal:
        prompt = (
            "You are a professional assistant. Read the following email and generate a reply that achieves the following goal.\n"
            f"Incoming email:\n{incoming_email}\n"
            f"Goal:\n{desired_goal}\n"
            "Reply:"
        )
        try:
            response = ollama.generate(model="gemma3:4b", prompt=prompt)
            st.success("Generated Reply:")
            st.write(response['response'])
        except Exception as e:
            st.error(f"Error generating reply: {e}")
    else:
        st.warning("Please provide both the incoming email and the desired goal.")
