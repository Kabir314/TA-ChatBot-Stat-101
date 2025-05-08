# Local LLM Teaching Assistant Chatbot

This project demonstrates how to run a local Large Language Model (LLM) and customize it into a teaching assistant that supports students in a college-level statistics course.

## Prerequisites
- Python 3.10+
- Git
- A modern GPU (or CPU with patience)
- Windows

## Installation

### 1. Install Requirements
```bash
py -m pip install -r requirements.txt
```

### 2. Clone the Web UI
```bash
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui
```

### 3. Download a Model (e.g., Mistral 7B in GGUF format)
Go to https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF and download a `.gguf` file.

Place it in the `models/` folder.

### 4. Launch the Web UI
```bash
python server.py --models mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

## Custom System Prompt
Go to the UI and add the following system prompt:

```
You are a teaching assistant for Prof. Smith's statistics course. Do not give direct answers to homework. Guide understanding and provide hints or expectations instead.
```

## Try it Out
Ask questions like:
- "What does question 4 on the homework want me to do?"
- "How should I approach a hypothesis test with unknown variance?"

---
