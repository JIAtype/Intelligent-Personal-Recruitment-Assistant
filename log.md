在项目根目录下打开终端，创建并激活虚拟环境，然后安装依赖：

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt



首先使用Ollama进行本地LLM调用。确保你已经安装了Ollama，并下载了Llama 3和Qwen模型
ollama pull llama3
ollama pull qwen