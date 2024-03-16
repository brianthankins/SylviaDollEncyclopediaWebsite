from PIL import Image
import streamlit as st

def image_processor(filepath, rotation, width=400, caption=""):
    org_img = Image.open(filepath)
    rotated_image = org_img.rotate(rotation)
    x = st.image(rotated_image, caption=caption, width=width)
    return x