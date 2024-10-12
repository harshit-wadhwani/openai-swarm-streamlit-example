import os
import streamlit as st
from agents import financial_planning_orchestrator_agent, client
from utils import pretty_print_messages

st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    st.sidebar.success("API Key set successfully!")
else:
    st.sidebar.warning("Please enter your OpenAI API Key")
    
st.title("Personal Finance AI")

agent = financial_planning_orchestrator_agent

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.run(agent=agent, messages=st.session_state.messages)
    message = response.messages
    agent = response.agent
    to_display = pretty_print_messages(messages=message)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(to_display)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": to_display})