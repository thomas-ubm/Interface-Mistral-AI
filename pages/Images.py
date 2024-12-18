import streamlit as st
from function import *
from mistralai import Mistral

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
api_keys = st.sidebar.text_input("apikeys")
client = Mistral(api_key=api_keys)

st.title("Analyse d'image")

st.subheader("Saisir ici le lien vers l'image à analyser")
#prompt = st.text_area("")
img_url = st.text_input()
# Création d'un bouton
if st.button("Analyser"):
  st.write(img_url)
  response = get_sentiment(client, img_url)
  st.write(response)


img_url = "https://plus.unsplash.com/premium_photo-1664474619075-644dd191935f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aW1hZ2V8ZW58MHx8MHx8fDA%3D"

def get_img(client, img_url):
  response = client.chat.complete(
      #model="mistral-larg-latest",
      model="pixtral-12b-2409",
      messages=[{
          
          #'role' : "system",
          #'content' : "Tu dois analyser des images....",
          
          'role' : "user",
          'content' : [{
                  'type' : 'text',
                  'text' : "Décris-moi ce qui se trouve sur l'image envoyée au format json : {'titre' : 'titre_image', 'description': 'descritpion_image'}"
          },
          {
                  'type' : 'image_url',
                  'image_url' : img_url
          }
          # On pourrait ajouter une image, pour demander une comparaison entre les deux...
          ]
      }]
  )
  response.choices[0].message.content
