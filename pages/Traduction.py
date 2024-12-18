import streamlit as st
from function import *
from mistralai import Mistral

# Titre à la page
#page_title="Ex-stream-ly Cool App",    page_icon="🧊",    layout="wide",
st.set_page_config("Titre à la page")

# Clé à utiliser : trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2
# api_keys = st.sidebar.text_input("apikeys")
api_keys = st.secrets["MISTRAL_API"]

client = Mistral(api_key=api_keys)

st.title("Traduction")

st.subheader("Saisir ici le texte à traduire")
prompt = st.text_area("")

# Création d'un bouton
if st.button("Traduire"):
  st.write(prompt)
  response = get_trad(client, prompt)
  st.write(response)

