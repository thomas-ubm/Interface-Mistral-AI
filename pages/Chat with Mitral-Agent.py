from function import *
from mistralai import Mistral
import streamlit as st

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
# api_keys = st.sidebar.text_input("apikeys")
api_keys = st.secrets["MISTRAL_API"]
client = Mistral(api_key=api_keys)


st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Création d'un bouton
if st.button("Vider l'historique"):
  st.session_state.messages = []


mistral-large-latest
ministral-8b-latest
mistral-small-latest


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

    # response = f"Echo: {prompt}"
    response = get_ner(client, prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

