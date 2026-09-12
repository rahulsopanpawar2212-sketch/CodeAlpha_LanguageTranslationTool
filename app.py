import streamlit as st
import requests

st.title("🌐 Language Translation Tool")

st.write("Translate text from one language to another.")

text = st.text_area(
    "Enter text to translate:",
    height=150
)

source_language = st.selectbox(
    "Source Language",
    ["English", "Hindi", "French", "Spanish", "German"]
)

target_language = st.selectbox(
    "Target Language",
    ["Hindi", "English", "French", "Spanish", "German"]
)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        language_codes = {
            "English": "en",
            "Hindi": "hi",
            "French": "fr",
            "Spanish": "es",
            "German": "de"
        }

        source_code = language_codes[source_language]
        target_code = language_codes[target_language]

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"{source_code}|{target_code}"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            translated_text = data["responseData"]["translatedText"]

            st.subheader("Translation")
            st.write(translated_text)

        else:
            st.error("Translation failed. Please try again.")