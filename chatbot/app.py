import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI  # Corrected import
from dotenv import load_dotenv
import os

# Load environment variables (such as your OpenAI API key)
load_dotenv()

# Set up the Streamlit page
st.set_page_config(page_title="Conversational Q&A Chatbot")  # Corrected set_page_config
st.header("Hey, Let's chat")

# Initialize the OpenAI chat model
chat = ChatOpenAI(temperature=0.5)  # Corrected to ChatOpenAI

# Initialize the conversation flow messages in session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant.")  # Default system message
    ]

# Function to get chat model response
def get_chatmodel_response(question):
    # Append the user's question as a human message
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    
    # Get the response from the chat model
    answer = chat(st.session_state['flowmessages'])
    
    # Append the AI's answer as an AI message
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    
    return answer.content

# Streamlit input/output handling
user_input = st.text_input("You: ", "")  # Input field for the user

if st.button("Send"):
    if user_input:
        response = get_chatmodel_response(user_input)
        st.write(f"AI: {response}")
