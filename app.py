#Q&A Chatbot

from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
os.environ['OPEN_API_KEY']='sk-aqARNNOsDM8RSdkdkkdkkdkdkdbkFJldtaWhrY4z0SQed76g0i'


##  function to load openAI model and get response

def get_openai_response(question):
    
    llm=OpenAI(openai_api_key=os.getenv('OPEN_API_KEY'),model_name="text-davinci-003",temperature=0.6)
    response=llm(question)
    return response
    
#initialize our streamlit app

st.set_page_config(page_title="Q&A demo")
st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)


submit=st.button("Ask the question")

#if ask submit button is called

if submit:
    st.subheader("The response is ")
    st.write(response)
    
