import streamlit as st
from function import *
from mistralai import Mistral

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
api_keys = st.sidebar.text_input("apikeys")
client = Mistral(api_key=api_keys)

st.title("Analyse d'éntités nommées")

st.subheader("Saisir ici le texte à analyser")
prompt = st.text_area("")

# Création d'un bouton
if st.button("Analyser"):
  st.write(prompt)
  response = get_ner(client, prompt)
  st.write(response)

# prompt1 = "Luc Martin habite à Marseille, 13000, et travaille avec Sophie Dupont qui vit à Bordeaux, 33000."
# prompt2 = "Paul Durand vit à Paris, 75001. Jeanne Morel habite à Nice, 06000."
