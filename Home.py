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
st.image('https://upload.wikimedia.org/wikipedia/fr/thumb/2/24/Universite_bordeaux-montaigne_2014_logo.svg/1200px-Universite_bordeaux-montaigne_2014_logo.svg.png')

# Création d'une vidéo
st.video('https://www.youtube.com/watch?v=Q4x_E1WD57s')

# Création d'un slider


# Lecture d'un fichier csv avec mandas

