from src.load_text import read_text_from_file
from src.prompt_templates import zero_shot, few_shot, chain_of_thought
from src.qa_engine import mock_generate, gemini_generate
from src.evaluate import save_results_to_csv

document = read_text_from_file("sample_docs/loan_agreement_summary.txt")
# print(loan_agreement)
zero_shot_results = {}
few_shot_results = {}
cot_results = {}

question = ""   
while True:
    question = input("You: ")
    if (question == "Goodbye!"):
        break

    # Use gemini_generate(prompt) for Gemini API
    # Use mock_generate(prompt) as placeholder when API output not needed. 
    zero_shot_results[question] = gemini_generate(zero_shot(document, question))
    few_shot_results[question] = gemini_generate(few_shot(document, question))
    cot_results[question] = gemini_generate(chain_of_thought(document, question))

    print("[ZERO-SHOT]", question)
    print(zero_shot_results[question])
    
    print("[FEW-SHOT]", question)
    print(few_shot_results[question])

    print("[CHAIN OF THOUGHT]", question)
    print(cot_results[question])
    print("\n")

    results = {
        "Zero-shot": zero_shot_results,
        "Few-shot": few_shot_results,
        "Chain of Thought": cot_results
    }
save_results_to_csv(results)