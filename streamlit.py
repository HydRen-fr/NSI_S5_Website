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

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar_crypte(text,dec):
  text_list = list(text)

  symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
  assert common_data(symbols, text_list) == False, "Caractères spéciaux non autorisés"

  for i in range(len(text_list)):
    if text_list[i] != " ":
        new_ele = alpha[(get_index(text_list[i], alpha) + dec) % len(alpha)]
        text_list[i] = new_ele

  new_text = "".join(text_list)

  return new_text

def cesar_decrypte(text,dec):
  text_list = list(text)

  symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
  assert common_data(symbols, text_list) == False, "Caractères spéciaux non autorisés"

  for i in range(len(text_list)):
    if text_list[i] != " ":
        new_ele = alpha[(get_index(text_list[i], alpha) - dec) % len(alpha)]
        text_list[i] = new_ele

  new_text = "".join(text_list)

  return new_text

# -------------------------------------------------------------------------------------------------------------------------------------------------  

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

# -------------------------------------------------------------------------------------------------------------------------------------------------

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    # Euclid
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def rsa_crypte(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher

def rsa_decrypte(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi




# CODE DU SITE

st.sidebar.title("Encodage Et Decodage Du Texte De Votre Choix")
algorithm = st.sidebar.selectbox("Choisissez Un Algorithme", ["Cesar", "Vigenere", "RSA"])
  
input_text = st.text_area("Votre Texte")
output_text = ""
  
if algorithm == "Cesar":
    if st.button("Encoder"):
        output_text = base64_encode(input_text)
    if st.button("Decoder"):
        output_text = base64_decode(input_text)

elif algorithm == "Vigenere":
    if st.button("Encoder"):
        output_text = rot13_encode(input_text)
    if st.button("Decoder"):
        output_text = rot13_decode(input_text)

elif algorithm == "RSA":
    if st.button("Encoder"):
        output_text = rot13_encode(input_text)
    if st.button("Decoder"):
        output_text = rot13_decode(input_text)
  
st.write(output_text)
