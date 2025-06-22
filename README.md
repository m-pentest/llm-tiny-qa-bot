# LLM Tiny QA Bot

This is a lightweight, beginner-friendly script that lets you query a local text file (`reference.txt`) using a language model (OpenAI or Ollama). It's a great way to learn the basics of retrieval-style LLM apps with minimal setup.

## What's Inside

- `qa_bot_openai.py` – Uses the OpenAI API to answer questions from your context  
- `qa_bot_ollama.py` – Uses a locally hosted LLM via Ollama (e.g., LLaMA3)  
- `reference.txt` – A sample file to serve as your knowledge base  
- `README.md` – Setup instructions and usage notes

## Setup and Usage

### 1. Install Python and Required Package

```bash
pip install requests
```

### 2. Prepare Your Reference File

Edit the file `reference.txt` with any content you want the bot to answer questions about.

Example:

```text
In agentic LLMs, memory is a persistence layer attackers can quietly poison for long-term control.
Unlike prompt injection, memory poisoning works over time by embedding misleading content that re-emerges in future steps.
```

### 3. Run the Bot

#### A. OpenAI API Method

```bash
export OPENAI_API_KEY=your_api_key_here
python qa_bot_openai.py
```

#### B. Ollama (Local) Method

```bash
brew install ollama
ollama run llama3
python qa_bot_ollama.py
```

## Example

```bash
$ python qa_bot_ollama.py
Ask your question: What is memory poisoning?
```

```text
Answer:
Memory poisoning is an attack where misleading or malicious content is embedded in an LLM’s memory over time. This can influence future outputs even after the initial interaction is over.
```

## Notes

- OpenAI usage may incur minimal API costs. You can manage usage limits on your [OpenAI account dashboard](https://platform.openai.com/account/usage).
- Ollama runs locally and is free, but performance may vary depending on your machine.
- This project is for personal use, learning, and experimentation.

## License

MIT — Free to use, modify, and share.
