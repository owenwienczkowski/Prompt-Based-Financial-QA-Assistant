from src.load_text import read_text_from_file
from src.prompt_templates import zero_shot, few_shot, chain_of_thought
from src.qa_engine import mock_generate

document = read_text_from_file("sample_docs/loan_agreement_summary.txt")
# print(loan_agreement)

prompt = zero_shot(document, "What is the penalty for a late payment?")
# print(prompt)

response = mock_generate(prompt)
# print(response)

question1 = "When must payments be received by?"
question2 = "When is the interest rate?"
question3 = "What is the payment frequency?"

questions = [question1, question2, question3]

zero_shot_results = {question: mock_generate(zero_shot(document, question)) for question in questions}

few_shot_results = {question: mock_generate(few_shot(document, question)) for question in questions}

cot_results = {question: mock_generate(chain_of_thought(document, question)) for question in questions}

for question in questions:
    print("[ZERO-SHOT]", question)
    print(zero_shot_results[question])
    
    print("[FEW-SHOT]", question)
    print(few_shot_results[question])

    print("[CHAIN OF THOUGHT]", question)
    print(cot_results[question])
    print("\n")
