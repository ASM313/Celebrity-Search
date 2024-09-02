from langchain_google_genai import GoogleGenerativeAI
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the GoogleGenerativeAI client with your API key
client = GoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_API_KEY"), model="gemini-pro")

