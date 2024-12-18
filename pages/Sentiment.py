import streamlit as st
from function import *
from mistralai import Mistral

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
api_keys = st.sidebar.text_input("apikeys")
client = Mistral(api_key=api_keys)

st.title("Analyse de sentiments")

st.subheader("Saisir ici le texte à analyser")
prompt = st.text_area("")

# Création d'un bouton
if st.button("Analyser"):
  st.write(prompt)
  response = get_sentiment(client, prompt)
  st.write(response)
