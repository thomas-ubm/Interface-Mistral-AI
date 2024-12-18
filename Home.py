import streamlit as st


# Création d'un titre
st.title('Interface-Mistral-AI')


# Création d'un sous titre
st.subheader("Mistral AI")


# Création d'une zone de texte
st.write("Introduction à mistral AI")

if st.checkbox("Afficher le contenu"):
  st.write("""
  # Titre
  ## Sous-titre
  **Text en gras** 
  `print("Hello World")`
  """)


# Zone de saisie de texte
user_name = st.text_input("Quel est votre nom?")
st.write(user_name)
print(user_name)


# Création d'un bouton
if st.button("Press OK"):
  st.write(user_name)


# Création d'une image
st.sidebar.image('https://upload.wikimedia.org/wikipedia/fr/thumb/2/24/Universite_bordeaux-montaigne_2014_logo.svg/1200px-Universite_bordeaux-montaigne_2014_logo.svg.png')

# Création d'une vidéo
st.sidebar.video("https://www.youtube.com/watch?v=sgnrL7yo1TE")


# Création d'un slider
user_age = st.slider("Quel est votre age ?", 18, 99, 30)

# Création d'une liste
user_country = st.selectbox("Selectionnez votre pays", ["France", "Espagne", "USA"])


# Lecture d'un fichier csv avec pandas
import pandas as pd
path_url = "https://raw.githubusercontent.com/Quera-fr/My-Credit/refs/heads/main/Analyse%20des%20donn%C3%A9es/test.csv"

df = pd.read_csv(path_url)

st.write(df, delimiter=';')

























