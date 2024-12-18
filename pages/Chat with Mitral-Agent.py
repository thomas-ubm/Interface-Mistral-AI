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

# Création d'un bouton
with open('histo.csv', mode='rb') as f:
    st.download_button(label='Télécharger l'historique', data=f, file_name='histo.csv')


choix = st.sidebar.radio("Choisissez : ", ["Modèle", "Agent"], index=0)



# Création d'une liste
user_model = st.sidebar.selectbox("Selectionnez un modèle", ["mistral-large-latest", "ministral-8b-latest", "mistral-small-latest"])

# Création d'une liste
user_agent = st.sidebar.selectbox("Selectionnez un agent", ["Culture-G", "Villes-par-habitants", "Emojibot"])

# Culture-G : ag:56f583a3:20241214:untitled-agent:5acbcaed
if user_agent == "Culture-G" :
    user_agent = "ag:56f583a3:20241214:untitled-agent:5acbcaed"

# Villes-par-habitants : ag:56f583a3:20241216:villes-par-habitants:babc8335
if user_agent == "Villes-par-habitants" :
    user_agent = "ag:56f583a3:20241216:villes-par-habitants:babc8335"

# Emojibot : ag:56f583a3:20241216:emojibot:3a89090a
if user_agent == "Emojibot" :
    user_agent = "ag:56f583a3:20241216:emojibot:3a89090a"



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
    if choix == "Modèle":
        st.write("Chat avec un modèle")
        response = get_chat(client, user_model, prompt)
    else:
        st.write("Chat avec un agent")
        response = get_agent(client, user_agent, prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

