import streamlit as st
import numpy as np
from PIL import Image
import tensorflow
import pickle

size = 80

def load_model(path):
    model_pkl = pickle.load(open(path, 'rb'))
    return model_pkl

def read_image(img):
    img = Image.open(img)
    img = img.convert('L')
    img = img.resize((size, size))
    img = np.array(img)
    img = img.astype('float32')
    return img

def rescale_img(img):
    img = np.asarray(img)
    img = img.reshape(1, size, size, 1)
    max_pixel_value = np.max(img)
    img = img/max_pixel_value
    return img

def reconstruct(img, model):
    recon_img = model.predict(img)
    return recon_img

def main():
    st.write("""
    # Fingerprint Reconstruction App

    You can reconstruct damaged or improperly printed fingerprints using this app.
    """)

    # Sidebar
    st.sidebar.header('User Input Interface')
    uploaded_file = st.sidebar.file_uploader("Upload your fingerprint here...")

    if uploaded_file is not None:
        model = load_model('model_original.pickle')
        image = read_image(uploaded_file)
        image = rescale_img(image)
        recon_image = reconstruct(image, model)
        recon_image = Image.fromarray((recon_image.reshape(size,size) * 255).astype(np.uint8))
        # recon_image = Image.fromarray(recon_image.reshape(size,size))
        recon_image = recon_image.convert('L')
    
    # Processing uploaded file
    original_img = Image.open(uploaded_file)
    original_img = original_img.convert('L')
    original_img = original_img.resize((size,size))

    # Centre
    original, recon = st.columns(2)
    with original:
        st.header("Original")
        st.image(original_img, caption="Original Image")
    with recon:
        st.header("Reconstruction")
        st.image(recon_image, caption="Reconstructed Image")

if __name__ == '__main__':
    main()