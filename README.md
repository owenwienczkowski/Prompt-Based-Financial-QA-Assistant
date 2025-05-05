# Prompt-Based Gemini QA Assistant

This project demonstrates how to build a lightweight, prompt-driven question-answering assistant using Google’s Gemini API. It uses structured or semi-structured textual documents to extract answers using multiple prompt engineering techniques.

## Project Goals

- Explore prompt engineering strategies (zero-shot, few-shot, chain-of-thought).
- Use LLMs (via Gemini API) to extract information from textual documents.
- Log results for history, evaluation, or general response comparison.
---

## Features

- Load and read mock textual documents.
- Apply different prompting techniques dynamically.
- Save responses to a `.csv` file.
- Swap between mock output and real API calls.
- CLI-based loop to simulate multi-query usage.

---

## Prompting Techniques Used

- **Zero-Shot:** Direct question → response with no context.
- **Few-Shot:** Injects 2–3 example QA pairs.
- **Chain-of-Thought (CoT):** Encourages intermediate reasoning steps.

---

## Directory Structure
Prompt-Based-Gemini-QA-Assistant/
│
├── sample_docs/ # Contains mock text document
│ └── loan_agreement_summary.txt
├── scripts/
│ └── run_qa.py # Main entrypoint for QA assistant
├── src/
│ ├── load_text.py # Loads document from file
│ ├── prompt_templates.py # Generates prompt strings
│ ├── qa_engine.py # Gemini and mock generators
│ └── evaluate.py # Result logging to CSV
├── qa_results.csv # Stores prompt-type → answer logs
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure .env
Create a .env file in the root directory:
```bash
GOOGLE_API_KEY=your_api_key_here
```

### 3. Run the assistant
```bash
python -m scripts.run_qa
```
You’ll be prompted to ask analytical questions like:

- *"What is the loan amount?"*

- *"When is the first payment due?"*

Type "Goodbye!" to exit.

🧾 Example Output
```csharp
[ZERO-SHOT] What is the interest rate?
1.2% annually, fixed.
```
```csharp
[FEW-SHOT] What is the interest rate?
The interest rate is 1.2% annually, fixed.
```
```csharp
[CHAIN OF THOUGHT] What is the interest rate?
I need to find the section that discusses the interest rate...
```

---

📦 Future Directions
- Add Streamlit/Gradio UI
- Support PDF chunking with LangChain
- Score prompts using GPTCritic or Gemini RAG evaluation
- Deploy with usage limits