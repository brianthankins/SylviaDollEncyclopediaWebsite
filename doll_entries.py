import streamlit as st
from imagefunctions import image_processor


def doll_entry(name, image_filepath1, rotation1, caption1, doll_description, linkpresent=False, link=""):
    st.header("", divider="rainbow")
    name = name.replace("_", " ")
    st.markdown(f"<h1 style='text-align: center; color: Pink;'>{name}</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        image_processor(filepath=image_filepath1, rotation=rotation1, caption=caption1)
        if linkpresent == True:
            st.link_button("Buy Here", link)
        else:
            pass
    with right_column:
        st.write(doll_description)
        st.write("##")
