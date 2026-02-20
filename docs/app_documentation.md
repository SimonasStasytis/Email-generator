
# App Documentation

## Overview
This Streamlit app generates professional email replies using Ollama and the gemma3:4b model. Users provide an incoming email and a desired goal for the reply, and the app produces a suggested response.


## How to Use
1. Paste the incoming email in "Email you received".
2. Enter your goal in "What do you want to achieve?".
3. Enter your name (optional) and your email.
4. Select the desired tone (Formal, Friendly, Short, Customer Support, Follow-up).
5. Adjust sidebar settings (Ollama URL, model, temperature, max tokens) if needed.
6. Click "Generate" to get a professional response.
7. Download the reply as a .txt file if desired.


## Technical Details
- Streamlit UI includes all required fields and settings per instructions.txt
- Sidebar for Ollama URL, model, temperature, and max tokens
- Tone selectbox influences reply style, grammar, and length
- Download button for generated reply
- Uses Ollama (local LLM) with gemma3:4b model
- Prompt is constructed to instruct the LLM to generate a reply based on the email, goal, user info, and tone

## Requirements
- Python
- Streamlit
- Ollama library
- gemma3:4b model

## References
- [Ollama Documentation](ollama_documentation.md)
- [Streamlit Documentation](streamlit_documentation.md)
