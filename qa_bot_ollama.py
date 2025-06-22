import requests
import json
 
def ask_ollama(context, question):
    prompt = f"""Use the following context to answer the question:\n\n{context}\n\nQ: {question}\nA:"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt},
        stream=True
    )

    output = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    output += data["response"]
            except Exception as e:
                print("Failed to parse line:", line)
                print("Error:", e)

    return output

with open("reference.txt", "r", encoding="utf-8") as f:
    context = f.read()
 
question = input("Ask your question: ")
answer = ask_ollama(context, question)
print("\nAnswer:\n", answer)
