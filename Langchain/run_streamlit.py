import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

st.title("T5 Chat Bot")

input_txt = st.text_input("Please enter your queries here...")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your name is T5 Assistant"),
        ("user", "{query}")
    ]
)

llm = Ollama(model="llama2:latest")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)

