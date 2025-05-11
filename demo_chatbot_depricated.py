## Depricated ##

## This file is depricated please refer to the console_chatbot python files


import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def run_demo():
    print("\nLoading model...")
    model_path = "./user_data/models"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Local model directory '{model_path}' not found. Please download and extract the model there.")
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")

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





from PyPDF2 import PdfReader
reader = PdfReader("lecture_notes.pdf")
full_text = "\n".join(page.extract_text() for page in reader.pages)


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_text(full_text)

embeddings = HuggingFaceEmbeddings()
db = FAISS.from_texts(chunks, embedding=embeddings)


query = "What is a Type II error?"
docs = db.similarity_search(query, k=2)
context = "\n".join([d.page_content for d in docs])

full_prompt = f"{system_prompt}\nContext:\n{context}\nStudent: {query}\nAssistant:"


if __name__ == "__main__":
    run_demo()
