#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:49:25 2024

@author: aidenguenther
"""
import streamlit as st
from st_social_media_links import SocialMediaIcons

st.title("Contact")

st.subheader("If you have any questions you can email our CIO, Daniel Hernandez, at virulahd@whitman.edu.")

st.image("field.jpg")

social_media_links = [
    "https://www.instagram.com/whitmaninvestmentcompany/",
    "https://www.linkedin.com/company/whitman-wic",
]

social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()



