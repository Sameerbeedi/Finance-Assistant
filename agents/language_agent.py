# agents/language_agent.py
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def generate_summary(retriever):
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run("What’s our risk exposure in Asia tech stocks?")
