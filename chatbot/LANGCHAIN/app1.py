## conversation Q&a chatbot 
import streamlit as st
from langchain.schema import HumanMessage , SystemMessage ,AIMessage
from langchain.chat_models import chatOpenAI

# from langchain.chat_model import chatOpenAI
# from langchain.chat_models import chatopenAI

## streamlit UI
st.setpage_config(page_title="Conversational Q&A Chatbot")
st.header("hey , Let's chat")

from dotenv import load_dotenv
load_dotenv()
import os

chat = chatOpenAI(temperature=0.5)

## function to load OpenAI model and get reponses
##quetion is that we get from the userend 
##acc to schema whenever we give a quetion that actually
##become a human message
# to provide a default domain ro cb , like act like a comedy cb, tht is sys mssg
# whenever cb or llb provide response , tht is AI mssg

if 'flowmessage' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="you are a comedian AI assitant ")
    ]
def get_chatmodel_response(quetion):

    # whenever we get the que
    st.session_state['flowmessages'].append(HumanMessage(content=quetion))
    # to get the answer 
    # here model doing prediction for all mssg tht are 
    # appended inside this particular session
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    
    return answer.content

'''
streamlit
Real-Time Updates:
Data Visualization
interactive web applications

'''


