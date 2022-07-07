import streamlit as st
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import pdfplumber
from PIL import Image


st.title("Resume Analyzer")
uploaded_file = None

rad =st.sidebar.radio("Navigation",["About this app","Try it"])

if rad == "About this app":
  st.header("About this app.")
  image = Image.open('image.jpeg')
  st.image(image, caption='Resume Analysis')

if rad == "Try it":
  
  uploaded_file = st.file_uploader("Upload your Resume(in PDF format)", type="pdf")
  skills = st.text_input("Enter Skills")
  resume_text = ""

  if uploaded_file is not None:
          with pdfplumber.open(uploaded_file) as pdf:
              first_page = pdf.pages[0]
              resume_text = first_page.extract_text()

  z = fuzz.token_set_ratio(skills, resume_text)


  st.write("Match = ",z,"%")

