
# Email-generator

## Overview
This Streamlit web application uses the Ollama library and the gemma3:4b model to generate professional email replies. The app takes an incoming email and a desired goal, then produces a suggested response.


## Features
- Streamlit UI with:
	- Text area: "Email you received"
	- Text area: "What do you want to achieve?"
	- Text input: "Your name (optional)"
	- Text input: "Your email"
	- Selectbox: "Tone" (Formal, Friendly, Short, Customer Support, Follow-up)
	- Output area for generated reply
	- Download button (.txt)
- Sidebar settings:
	- Ollama URL (default: http://127.0.0.1:11434)
	- Model name (default: gemma3:4b)
	- Temperature slider
	- Max tokens slider
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

1. Paste the incoming email into "Email you received".
2. Enter your goal in "What do you want to achieve?".
3. Enter your name (optional) and your email.
4. Select the desired tone.
5. Adjust sidebar settings if needed.
6. Click "Generate" to receive a professional response.
7. Download the reply as a .txt file if desired.

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
