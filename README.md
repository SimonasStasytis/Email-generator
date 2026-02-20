
# Email-generator

## Overview
This Streamlit web application uses the Ollama library and the gemma3:4b model to generate professional email replies. The app takes an incoming email and a desired goal, then produces a suggested response.

## Features
- Streamlit UI for easy input and output
- Integration with Ollama (local LLM)
- Uses gemma3:4b model for reply generation

## Setup
1. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
2. Ensure Ollama is running and the gemma3:4b model is available locally.
3. Run the app:
	```bash
	streamlit run app.py
	```

## Usage
1. Paste the incoming email into the provided text area.
2. Enter the desired goal for your reply.
3. Click "Generate Reply" to receive a professional response.

## Documentation
See the `docs` folder for detailed documentation:
- ollama_documentation.md
- streamlit_documentation.md
- app_documentation.md

## Requirements
- Python
- Streamlit
- Ollama library
- gemma3:4b model

## License
MIT
