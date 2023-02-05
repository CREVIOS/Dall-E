# -*- coding: utf-8 -*-
"""
@author: Asif
"""


import openai
import urllib.request
from PIL import Image
import streamlit as st



openai.api_key = "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"

def generate_image(image_description):

  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  

  img_url = img_response['data'][0]['url']

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img



# page title
st.title('Image Generation of DAll E')

# text input box for image recognition
img_description = st.text_input('Image Desription')

if st.button('Generate Image'):
    
    generated_img = generate_image(img_description)
    st.image(generated_img)
    
