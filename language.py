import streamlit as st
from translate import Translator
st.title("Language Translation app")
st.markdown("Maximum 500 characters")
st.markdown("Convert English to kannada")
inputtext = st.text_area("English",height=200)
translator = Translator(to_lang='kn', from_lang='en')
translation = translator.translate(inputtext)
st.text_area("ಕನ್ನಡ",translation,height=200)