import streamlit as st
from PIL import Image

st.subheader('Color to Grayscale Converter')

# Create a file uploader component allowing the user to upload a file
uploaded_img = st.file_uploader('Upload Image:')

with st.expander('Start Camera'):
    camera_image = st.camera_input('Camera')

# Check if the image exists meaning the user has uploaded a file
if uploaded_img:
    # Open the user uploaded image with PIL
    uploaded_img_open = Image.open(uploaded_img)
    # Convert the image to grayscale
    uploaded_gray_img = uploaded_img_open.convert('L')
    # Display the grayscale image on the webpage
    st.image(uploaded_gray_img)

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    img = Image.open(camera_image)
    # Convert the image to grayscale
    gray_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_img)