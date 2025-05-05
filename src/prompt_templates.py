def zero_shot(doc, question):
    prompt = f"Use the following document to answer the question:\nDocument: {doc}\nQuestion:{question}\nAnswer: "
    return prompt

def few_shot(doc, question):
    prompt = f"""Use the following document to answer the question:

    Document: {doc}

    Question: What is the penalty for a late payment?
    Answer: The penalty for a late fee is $25.

    Question: When is the first payment due?
    Answer: The first payment is due on November 1, 2025.

    Question: What is the loan amount?
    Answer: The loan amount is for $50,000.

    Question: {question}
    Answer: """
    return prompt

def chain_of_thought(doc, question):
    prompt = f"""Use the following document to answer the question:

    Document: {doc}

    Question: What is the penalty for a late payment?
    First reason through the document. Then provide your answer.
    Answer: I should first find the section related to penalties. Looking at the document, this is "Penalty Clauses". The document states explicitly that "A late payment fee of $25 will be assessed for any payment received after a 5-day grace period". Therefore, the penalty for a late payment is a $25 fee.
    Question: When is the first payment due?
    Let's think step by step.
    Answer: I need to locate where in the document the payment schedule is outlined. This seems to be under the "Repayment Terms" section. The document states "First payment due: November 1, 2025". Therefore, the first payment is due November 1, 2025.
    Question: What is the loan amount?
    Explain your reasoning before giving the final answer.
    Answer: I must first determine where in the document the loan financials are detailed. This content appears to be in the "Loan Terms" section. The document directly expresses "Loan Amount: $50,000". Therefore, the loan amount is for $50,000.
    Question: {question}
    Answer: """
    return prompt
