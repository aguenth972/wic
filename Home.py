#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:15:05 2024

@author: aidenguenther
"""
import streamlit as st
from PIL import Image
from st_social_media_links import SocialMediaIcons
import base64

# Set page configuration (must be the first Streamlit command)
##Header
image = Image.open('Logo2.png')
max_size = (200, 200)
image.thumbnail(max_size)

col1, col2, col3 = st.columns(3)

with col1:
    st.title("Welcome", anchor=False)

with col3:
    st.image(image)


image = Image.open('baloons.jpg')
st.image(image, use_column_width=True)


st.header("The Whitman Investment Company (WIC)")










# Social media links
social_media_links = [
    "https://www.instagram.com/whitmaninvestmentcompany/",
    "https://www.linkedin.com/company/whitman-wic",
]

social_media_icons = SocialMediaIcons(social_media_links)

# Render social media icons
social_media_icons.render()
