#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:21:09 2024

@author: aidenguenther
"""
import streamlit as st
from PIL import Image
from st_social_media_links import SocialMediaIcons

##Header
image = Image.open('Logo2.png')
max_size = (200, 200)
image.thumbnail(max_size)

col1, col2, col3 = st.columns(3)

with col1:
    st.title("Meetings", anchor=False)

with col3:
    st.image(image)

st.image("map.jpg")

st.subheader("We meet every **Wednesday** in **Maxey Hall 207**.", anchor=False)

social_media_links = [
    "https://www.instagram.com/whitmaninvestmentcompany/",
    "https://www.linkedin.com/company/whitman-wic",
]

social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()