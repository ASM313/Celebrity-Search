from langchain_google_genai import GoogleGenerativeAI
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the GoogleGenerativeAI client with your API key
client = GoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_API_KEY"), model="gemini-pro")


# Set the title of the Streamlit app
st.title("Gemini-LangChain")

# Create a text input field for user queries
input_text = st.text_input("Search anything")

# If there's input text from the user, process the request
if input_text:
    # Make a request to the GoogleGenerativeAI client
    response = client(input_text)
    
    # Display the response in the Streamlit app
    st.write(response)
