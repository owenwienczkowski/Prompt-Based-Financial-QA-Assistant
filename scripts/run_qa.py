from src.load_text import read_text_from_file
from src.prompt_templates import zero_shot, few_shot, chain_of_thought
from src.qa_engine import mock_generate, gemini_generate

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

zero_shot_results = {question: gemini_generate(zero_shot(document, question)) for question in questions}

few_shot_results = {question: gemini_generate(few_shot(document, question)) for question in questions}

cot_results = {question: gemini_generate(chain_of_thought(document, question)) for question in questions}

for question in questions:
    print("[ZERO-SHOT]", question)
    print(zero_shot_results[question])
    
    print("[FEW-SHOT]", question)
    print(few_shot_results[question])

    print("[CHAIN OF THOUGHT]", question)
    print(cot_results[question])
    print("\n")


'''Sample Outputs
[ZERO-SHOT] When must payments be received by?
Payments must be received by the 5th day of each month.

[FEW-SHOT] When must payments be received by?
Payments must be received by the 5th day of each month.

[CHAIN OF THOUGHT] When must payments be received by?
The section "Repayment Terms" specifies when payments must be received. 
It states, "Monthly payments must be received by the 5th day of each month".  
Therefore, payments must be received by the 5th of each month.

----

[ZERO-SHOT] When is the interest rate?
1.2% annually, fixed.

[FEW-SHOT] When is the interest rate?
The interest rate is 1.2% annually, fixed.

[CHAIN OF THOUGHT] When is the interest rate?
I need to find the section that discusses the interest rate. 
This information is located under the "Loan Terms" section.  
The document states "Interest Rate: 1.2% annually, fixed". 
Therefore, the interest rate is 1.2% per year, and it's a fixed rate.

----

[ZERO-SHOT] What is the payment frequency?
Monthly

[FEW-SHOT] What is the payment frequency?
The payment frequency is monthly.

[CHAIN OF THOUGHT] What is the payment frequency?
Let's think step by step.
The payment frequency is detailed in the "Loan Terms" section of the agreement. 
The document specifies "Payment Frequency: Monthly".  
Therefore, the payment frequency is monthly.

'''