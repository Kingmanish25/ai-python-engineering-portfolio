from langchain.llms import Ollama

def load_llm():

    llm = Ollama(
        model="llama3"
    )

    return llm
