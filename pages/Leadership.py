#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:31:46 2024

@author: aidenguenther
"""
import os
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


# Function to open and resize images
def open_and_resize_image(image_path, size=(200, 200)):
    try:
        image = Image.open(image_path)
        image = image.resize(size)
        return image
    except FileNotFoundError:
        st.write(f"Error: File not found at {image_path}")
        return None
    except Exception as e:
        st.write(f"An error occurred: {e}")
        return None

## Header
header_image = ('/Users/aidenguenther/Desktop/wic_app/Logo2.png')
if header_image:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.title("Leadership", anchor=False)

    with col3:
        st.image(header_image)

## Executive Board Members
st.subheader("Executive Board")

# Sample data for executive board members
executive_board = [
    {
        "name": "Beatrice Archer",
        "position": "CEO",
        "image": '/Users/aidenguenther/Desktop/wic_app/pages/beatrice_headshot.jpg'
    },
    {
        "name": "Hamze Haashi",
        "position": "CFO",
        "image": "/Users/aidenguenther/Desktop/wic_app/pages/hamze_headshot.jpg"
    },
    {
        "name": "Aiden Guenther",
        "position": "COO",
        "image": "/Users/aidenguenther/Desktop/wic_app/pages/aiden_headshot2.jpg"
    },
    {
        "name": "Daniel Virula Hernandez",
        "position": "CIO",
        "image": "/Users/aidenguenther/Desktop/wic_app/pages/daniel_headshot.jpg"
    }
]

# Creating columns for each member
cols = st.columns(4)

# Loop through each member and display their information
for col, member in zip(cols, executive_board):
    with col:
        resized_image = open_and_resize_image(member["image"])
        if resized_image:
            st.image(resized_image)
            st.subheader(member["name"])
            st.write(f"**{member['position']}**")
