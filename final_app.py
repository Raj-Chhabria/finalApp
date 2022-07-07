import streamlit as st
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import pdfplumber
from PIL import Image
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import jellyfish

stop_words = set(stopwords.words('english'))
st.title("Resume Analyzer")
filtered_sentence = ""
resume_text = ""
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


  word_tokens = word_tokenize(skills)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence = []
  for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  def listToString(s):
   
    # initialize an empty string
    str1 = ""
   
    # traverse in the string 
    for ele in s:
        str1 += ele 
   
    # return string 
    return str1
  ans = listToString(filtered_sentence)
  #z = fuzz.token_set_ratio(filtered_sentence, resume_text)
  z = jellyfish.jaro_distance(ans,resume_text)
  z = z*100
  output = round(z,2)
  st.write("Match = ",output,"%")

