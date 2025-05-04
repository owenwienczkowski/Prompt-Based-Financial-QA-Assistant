from src.load_text import read_text_from_file
from src.prompt_templates import zero_shot
from src.qa_engine import mock_generate

loan_agreement = read_text_from_file("sample_docs/loan_agreement_summary.txt")
# print(loan_agreement)

prompt = zero_shot(loan_agreement, "What is the penalty for a late payment?")
# print(prompt)

response = mock_generate(prompt)
print(response)