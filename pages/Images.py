import streamlit as st
from function import *
from mistralai import Mistral

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
api_keys = st.sidebar.text_input("apikeys")
client = Mistral(api_key=api_keys)


  

st.title("Analyse d'image")

st.subheader("Saisir ici le lien vers l'image à analyser")
#prompt = st.text_area("")
img_url = st.text_input("")
# Création d'un bouton
if st.button("Analyser"):
  st.write(img_url)
  response = get_sentiment(client, img_url)
  st.write(response)


# img_url = "https://plus.unsplash.com/premium_photo-1664474619075-644dd191935f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aW1hZ2V8ZW58MHx8MHx8fDA%3D"

