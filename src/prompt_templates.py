def zero_shot(data, question):
    prompt = f"Use the following document to answer the question:\nDocument: {data}\nQuestion:{question}\nAnswer: "
    return prompt