# IMPORTS

import streamlit as st
import random
from random import *
import math

# FONCTIONS AIDE

def get_index(ele,py_list):
  index = 0

  for i in range(len(py_list)):
    if py_list[i] == ele:
      index = i

  return index

def common_data(list1, list2):
    result = False
  
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result 
                  
    return result

# ALGOS

def cesar_crypte(text, dec):
    new_text = ""

    for ele in text:

        if ele.isalpha():
            new_ele = chr((ord(ele.upper()) + dec - 65) % 26 + 65)
            if ele.isupper():
                new_text += new_ele
            else:
                new_text += new_ele.lower()

        else:
            new_text += ele

    return new_text

def cesar_decrypte(text, dec):
    new_text = ""

    for ele in text:

        if ele.isalpha():
            new_ele = chr((ord(ele.upper()) - dec - 65) % 26 + 65)
            if ele.isupper():
                new_text += new_ele
            else:
                new_text += new_ele.lower()

        else:
            new_text += ele

    return new_text

#----------------------------------------------

def vigenere_crypte(text, key):
    key_len = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    text = ''
    for i in range(len(text_int)):
        shift = key_int[i % key_len]
        text += chr((text_int[i] + shift) % 26 + 65)
    return text

def vigenere_decrypte(text, key):
    key_len = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    text = ''
    for i in range(len(text_int)):
        shift = key_int[i % key_len]
        text += chr((text_int[i] - shift) % 26 + 65)
    return text


# CODE DU SITE

st.sidebar.title("Cryptage Et Decryptage Du Texte De Votre Choix")
algorithm = st.sidebar.selectbox("Choisissez Un Algorithme", ["Cesar", "Vigenere"])
  
input_text = st.text_area("Votre Texte")
output_text = ""
  
if algorithm == "Cesar":
    if st.button("Crypter"):
        output_text = cesar_crypte(input_text)
    if st.button("Decrypter"):
        output_text = cesar_decrypte(input_text)

elif algorithm == "Vigenere":
    if st.button("Crypter"):
        output_text = vigenere_crypte(input_text)
    if st.button("Decrypter"):
        output_text = vigenere_decrypte(input_text)
  
st.write(output_text)
