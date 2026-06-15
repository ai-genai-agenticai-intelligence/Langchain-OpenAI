#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain .chat_models import ChatOpenAI

import streamlit as st
import os
#from dotenv import load_dotenv

os.environ["GOOGLE_API_KEY"] = "AIzaSyD83TsU7aB25CPcnHsouPRM_r5irdSWYIY"
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]= "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"
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am hear to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('LLM-OPENAI PROJECT CUSTOM GEMINI-2.5-flash BY ABHISHEK SAHOO')
input_text=st.text_input("How may I help you")

# openAI LLm 
#llm = ChatOpenAI(model= 'gpt-5.1',temperature=1)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.3)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))