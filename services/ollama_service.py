from pathlib import Path
import ollama

MODEL = "llama3.2:latest"

PROMPT = Path("prompts/mentor.txt").read_text()

def ask_llm(user_prompt: str):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response["message"]["content"]