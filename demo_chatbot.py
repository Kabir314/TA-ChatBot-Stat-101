import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def run_demo():
    print("\n🔧 Loading model...")
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    chat = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=300)

    print("\nTeaching Assistant Chatbot Ready!")
    print("Type 'exit' to quit.\n")

    system_prompt = (
        "You are a teaching assistant for Prof. Smith's statistics class. "
        "You must not give direct answers to homework questions. Instead, provide helpful guidance, clarify concepts, and explain expectations."
    )

    while True:
        user_input = input("Student: ")
        if user_input.lower() == "exit":
            break

        full_prompt = f"{system_prompt}\nStudent: {user_input}\nAssistant:"
        response = chat(full_prompt)[0]['generated_text'].split("Assistant:")[-1].strip()
        print(f"TA: {response}\n")

if __name__ == "__main__":
    run_demo()
