import streamlit as st
import pandas as pd 
from PIL import Image
from imagefunctions import image_processor
from doll_entries import doll_entry
import Doll_Description
from Doll_Description import *
import urls
from age import sylvia_age

st.set_page_config(page_title="Wild Rulers Rule", page_icon=':female_fairy:')#, layout='wide')

st.title("Wild Rulers Rule :female_fairy:")
st.write("##")

with st.sidebar:
    st.subheader("About Me")
    st.header("Sylvia May")
    image_processor("Images/aboutme.jpg", 0)
    
    st.write(f"Hello my name is Sylvia! I am {sylvia_age} years old.")
# with st.container():
#     doll_entry("Jessy", 'Images/Jessy.JPG', 270, "Jessy", doll_description=Doll_Description.Jessy)
#     doll_entry("Jessy & Sparks", 'Images/Jessy2.JPG', 270, "Me and my hound", doll_description=Doll_Description.JessySparks)

# with st.container():
#     doll_entry("Emerson", 'Images/Emerson.JPG', 270, "Emerson", doll_description=Doll_Description.Emerson, linkpresent=True, link=urls.emerson_amazon)

# with st.container():
#     doll_entry('Camille', 'Images/Camille.JPG', rotation1=270, caption1='Camille', doll_description=Doll_Description.Camille)

# with st.container():
#     doll_entry("Kit", 'Images/Kit.JPG', 270, 'Kit', Doll_Description.Kit)

# with st.container():
#     doll_entry("Aminna", 'Images/Aminna.JPG', 270, 'Aminna', Doll_Description.Aminna)

# with st.container():
#     doll_entry("Belle", 'Images/Belle.JPG', 270, 'Belle', Doll_Description.Belle)

# with st.container():
#     doll_entry("Charlie", 'Images/Charlie.JPG', 270, 'Charlie', Doll_Description.Charlie)

# with st.container():
#     doll_entry("James & Emily", 'Images/JamesEmily.JPG', 270, 'James & Emily', Doll_Description.JamesEmily)

# with st.container():
#     doll_entry("Buddy", 'Images/Buddy.JPG', 270, 'Buddy', Doll_Description.Buddy)

dolls = ['Jessy',
         'Jessy_And_Sparks', 
         'Emerson', 
         'Camille', 
         'Camille_And_Her_Baby_Unicorns',
         'Kit', 
         'Kit_And_Lightning',
         'Aminna',
         'Aminna_And_Woofles', 
         'Belle', 
         'Belle_And_Roary',
         'Charlie',
         'Charlie_And_Penguin', 
         'James_And_Emily',
         'Emily_James_And_Their_Baby_Unicorns', 
         'Buddy',
         'Buddy_With_Bunny']

for doll in dolls:
    with st.container():
        doll_entry(name=f"{doll}", image_filepath1=f"Images/{doll}.JPG", rotation1=270, caption1=f"", doll_description=eval(doll), )