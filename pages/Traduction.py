import streamlit as st
from function import get_ner
from mistralai import Mistral

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
api_keys = st.sidebar.text_input("apikeys")
client = Mistral(api_key=api_keys)

st.title('Traduction')

st.subtitle('Saisissez ici le texte à traduire')
prompt = st.text_area()

# Création d'un bouton
if st.button("Traduire"):
  st.write(prompt)
  response = get_ner(client, prompt)
  st.write(response)

