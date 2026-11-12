# gen_ai_app_using_ollama

# Generative AI Application using Streamlit and Ollama

## Project Overview

This project is a Generative AI application built using Streamlit, LangChain, and Ollama. It provides an interactive interface where users can enter prompts and receive AI-generated responses using locally running Large Language Models (LLMs).

The application demonstrates how to integrate open-source LLMs with Python to build a simple and interactive Generative AI application.

## Features

- Interactive user interface using Streamlit.
- Integration with locally running Ollama models.
- Prompt-based text generation.
- LangChain integration for managing prompts and model interactions.
- Real-time response generation.
- Local LLM execution without requiring a cloud-based API.

## Technologies Used

- Python
- Streamlit
- Ollama
- LangChain
- ChatPromptTemplate
- StrOutputParser
- LangSmith (for tracing and monitoring, if configured)

## Project Structure

```text
Gen_AI_App/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── ...
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Gen_AI_App
```

### 3. Create a Virtual Environment

```bash
conda create -n genai_env python=3.11
```

### 4. Activate the Environment

```bash
conda activate genai_env
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install and Run Ollama

Download Ollama from:

https://ollama.com/

Pull the required model:

```bash
ollama pull gemma:2b
```

Make sure Ollama is running before starting the application.

### 7. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. The user enters a prompt through the Streamlit interface.
2. The prompt is formatted using LangChain's ChatPromptTemplate.
3. The formatted prompt is passed to the Ollama language model.
4. Ollama processes the prompt using the locally running LLM.
5. StrOutputParser converts the model output into a readable string.
6. Streamlit displays the generated response to the user.

## Learning Outcomes

- Understanding Large Language Models (LLMs).
- Working with locally hosted open-source models.
- Integrating Ollama with LangChain.
- Creating interactive AI applications using Streamlit.
- Understanding prompt templates and output parsers.
- Building applications with Generative AI technologies.

## Future Improvements

- Add conversation history and chat memory.
- Support multiple Ollama models.
- Add document-based question answering using RAG.
- Improve prompt customization.
- Integrate LangSmith for application tracing and monitoring.
- GitHub: https://github.com/Shivangi42
- LinkedIn: https://www.linkedin.com/in/shivangi-soni-b488b636a/
