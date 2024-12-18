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

# prompt1 = "J'ai passé une journée incroyable dans ce restaurant, le service était impeccable et les plats délicieux. Je reviendrai sans hésiter !"
# prompt2 = "C'était une expérience horrible, le personnel était désagréable et la nourriture immangeable. Je ne recommande absolument pas."
# prompt3 = "L'hôtel était correct, rien d'exceptionnel, mais il correspondait à ce que j'attendais pour ce prix."
