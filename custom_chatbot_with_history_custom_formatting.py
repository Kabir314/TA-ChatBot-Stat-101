from llama_cpp import Llama

# === Model Config ===
llm = Llama(
    model_path="./user_data/models/mistral-7b-instruct-v0.1.Q5_K_M.gguf",  # Replace with your model path
    n_ctx=2048,
    n_threads=4,
)

# === SYSTEM PROMPT ===
system_prompt = "You are a helpful and knowledgeable assistant designed for local use. Be concise, polite, and informative."

# === History Buffer ===
conversation_history = []

# === Prompt Constructor ===
def build_prompt(system_prompt, history, user_input):
    """
    Constructs a prompt in the form:
    [INST] <<SYS>> system_prompt <</SYS>> user: ... bot: ... user: current_input [/INST]
    """
    prompt = f"[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n"
    for i, (user, bot) in enumerate(history):
        prompt += f"user: {user}\nbot: {bot}\n"
    prompt += f"user: {user_input} [/INST]"
    return prompt

def build_alpaca_prompt(system_prompt, history, user_input):
    # prompt = "<s>"  # Start of prompt, lamma.cpp automatically prepends the s tag
    prompt = "" 

    if system_prompt:
        prompt += f"### System:\n{system_prompt}\n"

    for user_msg, bot_msg in history:
        prompt += f"### User:\n{user_msg}\n### Assistant:\n{bot_msg}\n"

    prompt += f"### User:\n{user_input}\n### Assistant:\n"
    return prompt

def build_custom_prompt(system_prompt, history, user_input):
    prompt = ""  # Start of prompt

    if system_prompt:
        prompt += f"\n{system_prompt}\n"

    #Intruction Template:
    prompt += "This is the chat bot terminal users please type your query and assitant will answer:\n"
    
    for user_msg, bot_msg in history:
        prompt += f"User:\n{user_msg}\nAssistant:\n{bot_msg}\n"

    prompt += f"User:\n{user_input}\nAssistant:\n"
    return prompt
# === Interactive Loop ===
print("Learning Chatbot: Type 'exit' to stop.")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    full_prompt = build_prompt(system_prompt, conversation_history, user_input)

    response = llm(
        prompt=full_prompt,
        max_tokens=256,
        stop=["</s>"]
        # stop=["### User:", "### System:", "</s>"] # Custom Prompt Stopping. 
    )

    bot_reply = response["choices"][0]["text"].strip()
    print(f"Bot: {bot_reply}")

    # Update context
    conversation_history.append((user_input, bot_reply))

filename = input("Enter filename to save chat log (e.g., `chat1.txt`): ").strip()

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"System Prompt:\n{system_prompt}\n\n")
    # Custom Prompt:
    # f.write(f"Addtional Templating: This is the chat bot terminal users please type your query and assitant will answer:\n")
    for user_msg, bot_msg in conversation_history:
        f.write(f"User Input: {user_msg}\n")
        f.write(f"Bot Messeage: {bot_msg}\n\n")

print(f"Conversation saved to {filename}")
