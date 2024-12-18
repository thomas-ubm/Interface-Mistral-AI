import streamlit as st
from function import get_ner
from mistralai import Mistral

api_keys = st.text_input("apikeys")
client = Mistral(api_key=api_keys)

prompt = st.text_area("""


""")

response = get_ner(client, prompt)


st.title('Traduction')

st.write(response)
