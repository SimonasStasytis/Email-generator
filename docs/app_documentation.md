
# App Documentation

## Overview
This Streamlit app generates professional email replies using Ollama and the gemma3:4b model. Users provide an incoming email and a desired goal for the reply, and the app produces a suggested response.

## How to Use
1. Paste the incoming email in the text area.
2. Enter your desired goal for the reply.
3. Click "Generate Reply" to get a professional response.

## Technical Details
- Uses Streamlit for the web interface.
- Uses Ollama (local LLM) with gemma3:4b model.
- Prompt is constructed to instruct the LLM to generate a reply based on the email and goal.

## Requirements
- Python
- Streamlit
- Ollama library
- gemma3:4b model

## References
- [Ollama Documentation](ollama_documentation.md)
- [Streamlit Documentation](streamlit_documentation.md)
