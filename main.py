# Integrate this app to OpenAI API
import os
from langchain.llms import *  
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 


from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-pro")


# streamlit app

st.title("Celeb Search")

input_text = st.text_input("Search any celeb")

# OpenAI LLM

openai_llm=OpenAI(temperature=0.7)

if input_text:
    st.write(openai_llm(input_text))
