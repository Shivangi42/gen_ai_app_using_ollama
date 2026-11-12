
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT2")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("human", "Question: {question}")
])

# Streamlit Framework
st.title("LangChain Demo with Gemma")
input_text = st.text_input("What question do you have in mind?")

# Ollama Model
llm = Ollama(model="gemma:2b")

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
