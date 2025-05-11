from llama_cpp import Llama

# Load the model
llm = Llama(
    model_path="./user_data/models/mistral-7b-instruct-v0.1.Q5_K_M.gguf",  # Change this path to your GGUF file
    n_ctx=2048,  # context length
    n_threads=4,  # adjust based on your CPU
)
system_prompt = ""
conversation_history = []
# Start a chat loop
print("Local LLM Chatbot. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    output = llm(
        f"[INST] {user_input} [/INST]",
        max_tokens=256,
        stop=["</s>"],  # Stop generation on this token if needed
    )

    response = output["choices"][0]["text"].strip()
    print("Bot:", response)
    conversation_history.append((user_input, response))

# === Save Conversation on Exit ===
filename = input("Enter filename to save chat log (e.g., `chat1.txt`): ").strip()

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"System Prompt:\n{system_prompt}\n\n")
    for user_msg, bot_msg in conversation_history:
        f.write(f"User Input: {user_msg}\n")
        f.write(f"Bot Messeage: {bot_msg}\n\n")

print(f"Conversation saved to {filename}")
