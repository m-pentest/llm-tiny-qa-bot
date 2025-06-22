import os
from openai import OpenAI
 
# Load OpenAI key (set this in your environment or hardcode for testing)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("reference.txt", "r", encoding="utf-8") as f:
    context = f.read()

question = input("Ask your question: ")

prompt = f"""
Use the following context to answer the question:

{context}

Q: {question}
A:
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nAnswer:\n", response.choices[0].message.content)
