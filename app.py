import streamlit as st
import tensorflow as tf
import numpy as np
import pickle

# Load assets
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('urdu_poetry_lstm.h5')

model = load_model()
char_to_idx, idx_to_char = pickle.load(open('mappings.pkl', 'rb'))

# Generation function (same as Part 3)
def generate_poem(...): ...

# Streamlit UI
st.title('Roman-Urdu Poetry Generator ✨')

seed_text = st.text_input('Enter starting words:', 'mohabbat')
temperature = st.slider('Creativity Level:', 0.1, 2.0, 0.8)

if st.button('Generate Poetry'):
    generated = generate_poem(
        seed_text.lower(),
        model,
        temperature=temperature
    )
    st.subheader('Generated Poem:')
    st.text(generated)
