import streamlit as st
from resnetClass import Classifier
from PIL import Image
import os

images = os.listdir('images/')
with st.sidebar:
    st.markdown(':red[Drag and Drop] a sample **picture**')
    for i in range(10):
        im = Image.open(f'images/{images[i]}', 'r').resize((230,230))
        st.image(im)

st.markdown("# :blue[Select a picture, it will tell you whether food or not.]")
image_file = st.file_uploader(":green[Upload Image file here]", 
                              type=['jpg', 'png', 'jpeg'], 
                              help='Drag and Drop an image',
                              )
col1, col2 = st.columns(2) 
if image_file != None:
    with col1:
        st.image(Image.open(image_file, 'r').resize((180,180)))
    img_data = Classifier.getImageData(image_file)
    prediction = Classifier.IsFood(img_data)
    with col2:
        if prediction == 'food':
            st.markdown("## :green[The picture shows kind of food..]")
        else:
            st.markdown("## :green[It seems no food in the picture.]")