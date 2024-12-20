import streamlit as st
import requests

st.title("Documentation")


# Création d'un bouton
if st.button("Afficher la doc"):
  #st.write(prompt)
  response = requests.get("http://127.0.0.1:8000/docs")
  st.write(response.text)
  




# prompt1 = "J'ai passé une journée incroyable dans ce restaurant, le service était impeccable et les plats délicieux. Je reviendrai sans hésiter !"
# prompt2 = "C'était une expérience horrible, le personnel était désagréable et la nourriture immangeable. Je ne recommande absolument pas."
# prompt3 = "L'hôtel était correct, rien d'exceptionnel, mais il correspondait à ce que j'attendais pour ce prix."
