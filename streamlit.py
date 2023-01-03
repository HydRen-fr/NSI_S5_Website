# IMPORTS

import streamlit as st
from random import *
from math import *

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

    # Make sure that the key only contains uppercase letters
    key = key.upper()
    key = key.replace(' ', '')

    key_len = len(key)
    key_int = [ord(i) - 65 for i in key]  # Shift the ordinal values to start at 0
    text_int = [ord(i) for i in text]
    crypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():  # Only encrypt letters, not spaces or other characters
            shift = key_int[key_index % key_len]
            crypted_char = chr((ord(char) + shift - 65) % 26 + 65)
            key_index += 1
        else:
            crypted_char = char
        crypted_text += crypted_char
    return crypted_text

def vigenere_decrypte(text, key):
    '''
    Fonction de décryptage de Vigenère
    text (str) : message crypté
    key (str) : clé de décryptage à utiliser
    Retourne (str) : message décrypté
    '''

    # Make sure that the key only contains uppercase letters
    key = key.upper()
    key = key.replace(' ', '')

    key_len = len(key)
    key_int = [ord(i) - 65 for i in key]  # Shift the ordinal values to start at 0
    text_int = [ord(i) for i in text]
    decrypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():  # Only decrypt letters, not spaces or other characters
            shift = key_int[key_index % key_len]
            decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            key_index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def rsa_keygen(p, q):
    '''
    Fonction de génération de clés RSA
    p (int) : premier nombre premier
    q (int) : deuxième nombre premier
    Retourne (tuple) : clés publique et privée sous forme de tuple (e, n), (d, n)
    '''
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    # Compute the secret exponent d such that d * e = 1 (mod phi(n))
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return (e, n), (d, n)

def rsa_crypte(text, e, n):
    '''
    Fonction de cryptage RSA
    text (str) : message à crypter
    e (int) : exposant de cryptage
    n (int) : module
    Retourne (list) : message crypté sous forme de liste de nombres
    '''
    text_int = [ord(i) for i in text]
    encrypted_text = [pow(i, e, n) for i in text_int]
    return encrypted_text

def rsa_decrypte(encrypted_text, d, n):
    '''
    Fonction de décryptage RSA
    encrypted_text (list) : message crypté sous forme de liste de nombres
    d (int) : exposant de décryptage
    n (int) : module
    Retourne (str) : message décrypté
    '''
    decrypted_text = [chr(pow(i, d, n)) for i in encrypted_text]
    return ''.join(decrypted_text)



# CODE DU SITE

st.sidebar.header("Cryptage/décryptage du message")

algorithm = st.sidebar.selectbox("Algorithme", ["César", "Vigenère", "RSA"],
                                 format_func=lambda x: x + ' ?')
st.sidebar.info('Le chiffre de César consiste à décaler chaque lettre du message de N positions dans l\'alphabet')
st.sidebar.info('Le chiffre de Vigenère consiste à utiliser une clé pour crypter le message avec le chiffre de César')
st.sidebar.info('RSA est un algorithme de cryptage asymétrique qui utilise une clé publique et une clé privée')

text = st.sidebar.text_input("Message")

if algorithm == "César":
    dec = st.sidebar.number_input("Décalage", min_value=0, max_value=25)

elif algorithm == "Vigenère":
    key = st.sidebar.text_input("Clé")

elif algorithm == "RSA":
    p = st.sidebar.number_input("Premier nombre premier", min_value=2, max_value=1000)
    q = st.sidebar.number_input("Deuxième nombre premier", min_value=2, max_value=1000)
    # Generate the keys
    public_key, private_key = rsa_keygen(p, q)

if st.sidebar.button("Crypter"):
    if algorithm == "César":
        crypte = cesar_crypte(text, dec)
    elif algorithm == "Vigenère":
        crypte = vigenere_crypte(text, key)
    elif algorithm == "RSA":
        crypte = rsa_crypte(text, *public_key)

if st.sidebar.button("Décrypter"):
    if algorithm == "César":
        decrypte = cesar_decrypte(text, dec)
    elif algorithm == "Vigenère":
        decrypte = vigenere_decrypte(text, key)
    elif algorithm == "RSA":
        decrypte = rsa_decrypte(text, *private_key)
