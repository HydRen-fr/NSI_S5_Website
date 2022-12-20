# IMPORTS

import streamlit as st
from random import *

# ALGOS

def cesar_crypte(text, dec):
    '''
    Fonction de cryptage de César
    text (str) : message à crypter
    dec (int) : décalage à utiliser pour le cryptage
    Retourne (str) : message crypté
    '''

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
    '''
    Fonction de décryptage de César
    text (str) : message crypté
    dec (int) : décalage à utiliser pour le décryptage
    Retourne (str) : message décrypté
    '''

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

def vigenere_crypte(text, key):
    '''
    Fonction de cryptage de Vigenère
    text (str) : message à crypter
    key (str) : clé de cryptage à utiliser
    Retourne (str) : message crypté
    '''

    key_len = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    text = ''
    for i in range(len(text_int)):
        shift = key_int[i % key_len]
        text += chr((text_int[i] + shift) % 26 + 65)
    return text

def vigenere_decrypte(text, key):
    '''
    Fonction de décryptage de Vigenère
    text (str) : message crypté
    key (str) : clé de décryptage à utiliser
    Retourne (str) : message décrypté
    '''

    key_len = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    text = ''
    for i in range(len(text_int)):
        shift = key_int[i % key_len]
        text += chr((text_int[i] - shift) % 26 + 65)
    return text


# CODE DU SITE

st.sidebar.header("Cryptage/décryptage du message")


algorithm = st.sidebar.selectbox("Algorithme", ["César", "Vigenère"])
text = st.sidebar.text_input("Message")


if algorithm == "César":
    dec = st.sidebar.number_input("Décalage", min_value=0, max_value=25)

else:
    key = st.sidebar.text_input("Clé")


if st.sidebar.button("Crypter"):
    if algorithm == "César":
        crypte = cesar_crypte(text, dec)

    else:
        crypte = vigenere_crypte(text, key)
    st.success("Message crypté : {}".format(crypte))
    

if st.sidebar.button("Décrypter"):
    if algorithm == "César":
        decrypte = cesar_crypte(crypte, dec)

    else:
        decrypte = vigenere_decrypte(crypte, key)
    st.success("Message décrypté : {}".format(decrypte))
