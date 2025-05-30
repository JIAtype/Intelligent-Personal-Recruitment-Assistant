from flask import Flask, render_template, request, jsonify
import json
import os
from utils.llm_handler import get_llm_response_ollama, load_resume_data # Import Ollama version for now
# from dotenv import load_dotenv # For API keys if you switch to cloud APIs

# load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

# --- Load resume data for display ---
# We load it once at startup for efficiency
# The llm_handler also loads it, but this is for displaying on the page
try:
    with open('resume_data/resume_en.json', 'r', encoding='utf-8') as f:
        resume_display_en = json.load(f)
except Exception as e:
    print(f"Error loading English resume for display: {e}")
    resume_display_en = {"error": "Could not load English resume data."}

try:
    with open('resume_data/resume_zh.json', 'r', encoding='utf-8') as f:
        resume_display_zh = json.load(f)
except Exception as e:
    print(f"Error loading Chinese resume for display: {e}")
    resume_display_zh = {"error": "Could not load Chinese resume data."}
# --- End resume data loading for display ---


@app.route('/')
def index():
    # Default to English, or could try to guess from browser accept-language
    default_lang = request.args.get('lang', 'en')
    if default_lang == 'zh':
        resume_to_display = resume_display_zh
        current_lang = 'zh'
    else:
        resume_to_display = resume_display_en
        current_lang = 'en'
    
    # Pass the whole resume object and the current language to the template
    return render_template('index.html', resume=resume_to_display, current_lang=current_lang)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Here, you would choose between Ollama or an API call
    # For now, using Ollama from llm_handler
    ai_response = get_llm_response_ollama(user_message)
    
    # Example for API (you'd need to set API_KEY and ENDPOINT in .env or config)
    # LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
    # QWEN_API_KEY = os.getenv("QWEN_API_KEY")
    # lang = detect(user_message) # You'd need language detection here too
    # if lang == 'zh':
    #    ai_response = get_llm_response_api(user_message, QWEN_API_KEY, "QWEN_ENDPOINT")
    # else:
    #    ai_response = get_llm_response_api(user_message, LLAMA_API_KEY, "LLAMA_ENDPOINT")

    return jsonify({"reply": ai_response})

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Use a different port if 5000 is in use