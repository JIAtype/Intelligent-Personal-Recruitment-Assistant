import ollama
import json
import os
from langdetect import detect

# 加载简历数据
def load_resume_data(lang='en'):
    file_path = f"resume_data/resume_{lang}.json"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Resume file {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}.")
        return None

resume_data_en = load_resume_data('en')
resume_data_zh = load_resume_data('zh')

# 将简历数据转换为字符串格式，以便LLM理解
def format_resume_for_llm(resume_data):
    if not resume_data:
        return "Resume data is not available."
    # A simple way to format. You can make this more sophisticated.
    return json.dumps(resume_data, ensure_ascii=False, indent=2)

formatted_resume_en = format_resume_for_llm(resume_data_en)
formatted_resume_zh = format_resume_for_llm(resume_data_zh)

def get_llm_response_ollama(user_query: str):
    try:
        lang = detect(user_query)
    except Exception as e:
        print(f"Language detection failed: {e}. Defaulting to English.")
        lang = 'en' # Default to English if detection fails

    if lang == 'zh' or lang == 'zh-cn' or lang == 'zh-tw':
        model_name = "qwen:latest" # Or specify a version like qwen:7b
        resume_context = formatted_resume_zh
        system_prompt_template = """
        你是我的个人简历助手。请根据以下简历信息回答用户的问题。
        严格根据提供的简历信息回答，如果信息不在简历中，请明确说明。不要编造信息。

        简历信息：
        ---
        {resume_context}
        ---

        请用中文回答。
        """
    else:
        model_name = "llama3:latest" # Or specify a version like llama3:8b
        resume_context = formatted_resume_en
        system_prompt_template = """
        You are my personal resume assistant. Answer the user's questions based on the following resume information.
        Answer strictly based on the provided resume information. If the information is not in the resume, state that clearly. Do not make up information.

        Resume Information:
        ---
        {resume_context}
        ---

        Please answer in English.
        """
    
    if not resume_context or "not available" in resume_context:
         return "I'm sorry, but the resume data is currently unavailable. I cannot answer questions about it."


    prompt = system_prompt_template.format(resume_context=resume_context)

    print(f"--- Debug ---")
    print(f"Detected language: {lang}")
    print(f"Using model: {model_name}")
    # print(f"Using resume context (first 100 chars): {resume_context[:100]}")
    print(f"User query: {user_query}")
    print(f"--- End Debug ---")

    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_query},
            ],
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Error communicating with Ollama model {model_name}: {e}")
        return "Sorry, I encountered an error while processing your request with the AI model."

# 备选：使用云端API (示例 - 需自行替换为实际API调用逻辑)
# def get_llm_response_api(user_query: str, api_key: str, model_endpoint: str):
#     # This is a placeholder. You'll need to implement the actual API call
#     # using requests library for Llama 3 (e.g., Replicate, Groq) or Qwen (Alibaba Cloud).
#     # Remember to handle language detection and choose the correct model_endpoint and prompt.
#     import requests
#     headers = {"Authorization": f"Bearer {api_key}"}
#     payload = {
#         "model": "model_id_for_llama3_or_qwen", # specific to the API provider
#         "prompt": f"Context: [Your Resume Data]\n\nQuestion: {user_query}\n\nAnswer:",
#         "max_tokens": 150
#     }
#     try:
#         response = requests.post(model_endpoint, json=payload, headers=headers)
#         response.raise_for_status()
#         return response.json()["choices"][0]["text"] # This structure varies by API
#     except requests.exceptions.RequestException as e:
#         print(f"API request failed: {e}")
#         return "Sorry, I encountered an error with the API."


if __name__ == '__main__':
    # Test
    print("Testing English query:")
    print(get_llm_response_ollama("What is his experience?"))
    print("\nTesting Chinese query:")
    print(get_llm_response_ollama("他的工作经历是什么？"))
    print("\nTesting with missing info:")
    print(get_llm_response_ollama("What's his favorite color?"))