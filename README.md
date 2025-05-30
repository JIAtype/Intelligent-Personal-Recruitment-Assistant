# Personalized Resume with Bilingual AI Chatbot

This project showcases a personalized resume website integrated with a bilingual AI chatbot. Users can view resume information and interact with an AI assistant (powered by Llama 3 for English and Qwen for Chinese, or other selected LLMs) to ask questions about the resume content in real-time.

[View Live Demo](YOUR_DEPLOYED_LINK_HERE) <!-- Replace with your actual deployed link -->

## Features

*   **Bilingual Resume Display:** View resume details in English or Chinese.
*   **Interactive AI Chatbot:** Ask questions about the resume and get instant answers.
*   **Dual LLM Support:**
    *   Utilizes Llama 3 (or a similar model) for English queries.
    *   Utilizes Qwen (or a similar model) for Chinese queries.
    *   (You can specify the exact models you ended up using, e.g., Gemini via Google AI Studio, or models via Hugging Face Inference API)
*   **Dynamic Language Detection:** The backend automatically detects the language of the user's query to route it to the appropriate LLM.
*   **MCP (My Custom Prompt) / RAG-like Approach:** The LLMs are prompted with the resume content as context to provide accurate, resume-specific answers.
*   **Web Interface:** Built with Flask (Python) for the backend and HTML, CSS, JavaScript for the frontend.

## Tech Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML, CSS, JavaScript
*   **LLM Integration:**
    *   [Specify your choice: e.g., Ollama (for local Llama 3 & Qwen), Hugging Face Inference API, Google AI Studio (Gemini), etc.]
*   **Resume Data:** JSON format
*   **Language Detection:** `langdetect` Python library
*   **Deployment:** [Specify your deployment platform: e.g., Render, PythonAnywhere, Hugging Face Spaces, Google Cloud Run, etc.]

## Project Structure

Intelligent-Personal-Recruitment-Assistant/
├── app.py # Flask backend application
├── static/ # CSS, JS files
│ ├── css/style.css
│ └── js/script.js
├── templates/ # HTML templates
│ └── index.html
├── resume_data/ # Resume data in JSON
│ ├── resume_en.json
│ └── resume_zh.json
├── utils/ # Utility scripts
│ └── llm_handler.py # Logic for LLM interaction
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables (API keys)
├── Dockerfile # (Optional, if using Docker for deployment)
└── README.md

## Setup and Installation (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare Resume Data:**
    *   Edit `resume_data/resume_en.json` and `resume_data/resume_zh.json` with your personal information.

5.  **Configure LLM Access:**
    *   **If using Ollama (local):**
        *   Ensure Ollama is installed and running.
        *   Pull the required models:
            ```bash
            ollama pull llama3
            ollama pull qwen # or the specific qwen model you are using
            ```
    *   **If using Hugging Face Inference API / Google Gemini API / Other Cloud APIs:**
        *   Create a `.env` file in the project root by copying `.env.example`.
        *   Add your API keys to the `.env` file:
            ```
            # For Hugging Face
            HF_API_TOKEN="your_hf_api_token"

            # For Google Gemini
            GOOGLE_API_KEY="your_google_api_key"

            # Add other API keys if needed
            ```
        *   Ensure `utils/llm_handler.py` is configured to use your chosen API.

6.  **Run the Flask application:**
    ```bash
    python app.py
    ```

7.  Open your browser and navigate to `http://127.0.0.1:5001` (or the port specified in `app.py`).

## Deployment

This application can be deployed to various platforms like Render, PythonAnywhere, Google Cloud Run, or Hugging Face Spaces.

**General Steps for PaaS (e.g., Render):**

1.  Push your code to a Git repository (GitHub, GitLab).
2.  Connect your Git repository to the deployment platform.
3.  Configure the build command (e.g., `pip install -r requirements.txt`).
4.  Configure the start command (e.g., `gunicorn app:app`).
5.  Set up necessary environment variables (like `HF_API_TOKEN`, `GOOGLE_API_KEY`) on the platform.
6.  Deploy!

Refer to the specific documentation of your chosen platform for detailed instructions.

## How It Works

1.  The user visits the web page, which displays the resume (defaulting to English, switchable to Chinese).
2.  The resume content is loaded from `resume_data/*.json` files.
3.  The user types a question into the chat interface.
4.  The JavaScript frontend sends the user's message to the Flask backend (`/chat` endpoint).
5.  The backend detects the language of the query.
6.  Based on the language, the backend selects the appropriate LLM (Llama 3 for English, Qwen for Chinese).
7.  A prompt is constructed that includes the user's query and the relevant resume data (MCP/RAG).
8.  The backend sends this prompt to the chosen LLM (via local Ollama or a cloud API).
9.  The LLM generates a response.
10. The backend sends the LLM's response back to the frontend.
11. The JavaScript frontend displays the AI's reply in the chat window.

## Future Improvements

*   Streaming responses for a better chat experience.
*   Conversation history support.
*   More sophisticated RAG techniques for very long resumes (e.g., vector embeddings).
*   Enhanced UI/UX.
*   Admin panel to update resume data easily.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information (if you add one).

---

# 个性化简历与双语AI聊天机器人

本项目展示了一个集成了双语AI聊天机器人的个性化简历网站。用户可以查看简历信息，并与AI助手（英文请求由Llama 3支持，中文请求由Qwen支持，或您选择的其他大语言模型）进行实时对话，询问关于简历内容的问题。

[查看在线演示](DEPLOYED_LINK_HERE) <!-- 替换为您的实际部署链接 -->

## 功能特性

*   **双语简历展示：** 可查看英文或中文版的简历详情。
*   **交互式AI聊天机器人：** 针对简历内容提问并获得即时回答。
*   **双大语言模型支持：**
    *   使用 Llama 3 (或类似模型) 处理英文问询。
    *   使用 Qwen (或类似模型) 处理中文问询。
    *   (您可以具体说明您最终使用的模型，例如：通过Google AI Studio的Gemini，或通过Hugging Face Inference API的模型)
*   **动态语言检测：** 后端自动检测用户问题的语言，以将其路由到合适的LLM。
*   **MCP (我的定制提示) / 类RAG方法：** 将简历内容作为上下文提示LLM，以提供准确的、针对简历的回答。
*   **Web界面：** 后端使用Flask (Python) 构建，前端使用HTML, CSS, JavaScript。

## 技术栈

*   **后端：** Python, Flask
*   **前端：** HTML, CSS, JavaScript
*   **LLM集成：**
    *   [指明您的选择：例如，Ollama (本地运行Llama 3 & Qwen)，Hugging Face Inference API，Google AI Studio (Gemini) 等]
*   **简历数据：** JSON 格式
*   **语言检测：** `langdetect` Python库
*   **部署平台：** [指明您的部署平台：例如，Render, PythonAnywhere, Hugging Face Spaces, Google Cloud Run 等]

## 项目结构

Intelligent-Personal-Recruitment-Assistant/
├── app.py # Flask backend application
├── static/ # CSS, JS files
│ ├── css/style.css
│ └── js/script.js
├── templates/ # HTML templates
│ └── index.html
├── resume_data/ # Resume data in JSON
│ ├── resume_en.json
│ └── resume_zh.json
├── utils/ # Utility scripts
│ └── llm_handler.py # Logic for LLM interaction
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables (API keys)
├── Dockerfile # (Optional, if using Docker for deployment)
└── README.md


## 安装与本地运行

1.  **克隆仓库：**
    ```bash
    git clone https://github.com/您的用户名/您的仓库名.git
    cd 您的仓库名
    ```

2.  **创建并激活虚拟环境：**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **安装依赖：**
    ```bash
    pip install -r requirements.txt
    ```

4.  **准备简历数据：**
    *   编辑 `resume_data/resume_en.json` 和 `resume_data/resume_zh.json`，填入您的个人信息。

5.  **配置LLM访问：**
    *   **如果使用 Ollama (本地)：**
        *   确保已安装并运行Ollama。
        *   拉取所需模型：
            ```bash
            ollama pull llama3
            ollama pull qwen # 或您使用的特定qwen模型
            ```
    *   **如果使用 Hugging Face Inference API / Google Gemini API / 其他云API：**
        *   通过复制 `.env.example` 在项目根目录创建一个 `.env` 文件。
        *   将您的API密钥添加到 `.env` 文件中：
            ```
            # Hugging Face
            HF_API_TOKEN="your_hf_api_token"

            # Google Gemini
            GOOGLE_API_KEY="your_google_api_key"

            # 如果需要，添加其他API密钥
            ```
        *   确保 `utils/llm_handler.py` 已配置为使用您选择的API。

6.  **运行Flask应用：**
    ```bash
    python app.py
    ```

7.  打开浏览器并访问 `http://127.0.0.1:5001` (或在 `app.py` 中指定的端口)。

## 部署

此应用可以部署到多种平台，如 Render, PythonAnywhere, Google Cloud Run, 或 Hugging Face Spaces。

**PaaS平台通用步骤 (例如 Render)：**

1.  将您的代码推送到Git仓库 (GitHub, GitLab)。
2.  将您的Git仓库连接到部署平台。
3.  配置构建命令 (例如 `pip install -r requirements.txt`)。
4.  配置启动命令 (例如 `gunicorn app:app`)。
5.  在平台上设置必要的环境变量 (如 `HF_API_TOKEN`, `GOOGLE_API_KEY`)。
6.  部署！

请参考您选择的平台的具体文档以获取详细说明。

## 工作原理

1.  用户访问网页，网页显示简历（默认为英文，可切换为中文）。
2.  简历内容从 `resume_data/*.json` 文件加载。
3.  用户在聊天界面中输入问题。
4.  JavaScript前端将用户消息发送到Flask后端 (`/chat` 端点)。
5.  后端检测查询的语言。
6.  根据语言，后端选择合适的LLM（英文为Llama 3，中文为Qwen）。
7.  构造一个包含用户查询和相关简历数据（MCP/RAG）的提示。
8.  后端将此提示发送给选定的LLM（通过本地Ollama或云API）。
9.  LLM生成响应。
10. 后端将LLM的响应发送回前端。
11. JavaScript前端在聊天窗口中显示AI的回复。

## 未来改进方向

*   流式响应以改善聊天体验。
*   支持对话历史记录。
*   针对非常长的简历采用更高级的RAG技术（例如向量嵌入）。
*   增强UI/UX。
*   用于方便更新简历数据的管理面板。

## 贡献代码

欢迎贡献！请随时提交 Pull Request 或开启 Issue。

1.  Fork 本项目
2.  创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3.  提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4.  推送到分支 (`git push origin feature/AmazingFeature`)
5.  开启一个 Pull Request

## 许可证

使用 MIT 许可证发行。更多信息请参见 `LICENSE` 文件。