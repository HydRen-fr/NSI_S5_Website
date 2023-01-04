# IMPORTS

# On importe les bibliothèques nécessaires pour le code

import streamlit as st
from random import *
from math import *

# ALGOS

# On définit une fonction de cryptage de César

def cesar_crypte(text, dec):
    '''
    Fonction de cryptage de César
    text (str) : message à crypter
    dec (int) : décalage à utiliser pour le cryptage
    Retourne (str) : message crypté
    '''

    new_text = ""

    # On parcourt chaque élément du message à crypter
    for ele in text:
        # Si c'est une lettre
        if ele.isalpha():
            # On calcule le code ASCII du nouvel élément en faisant un décalage de "dec" lettres par rapport à l'élément d'origine
            new_ele = chr((ord(ele.upper()) + dec - 65) % 26 + 65)
            if ele.isupper():
                new_text += new_ele
            else:
                new_text += new_ele.lower()

        else:
            new_text += ele

    return new_text

# On définit une fonction de decryptage de César

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

# On définit une fonction de cryptage de Vigenère

def vigenere_crypte(text, key):
    '''
    Fonction de cryptage de Vigenère
    text (str) : message à crypter
    key (str) : clé de cryptage à utiliser
    Retourne (str) : message crypté
    '''

    # On s'assure que la clé ne contient que des lettres en majuscule
    key = key.upper()
    key = key.replace(' ', '')

    key_len = len(key)
    # On calcule les codes ASCII de chaque lettre de la clé en décalant les valeurs ordinales de 65 (pour qu'elles commencent à 0)
    key_int = [ord(i) - 65 for i in key]  
    text_int = [ord(i) for i in text]
    crypted_text = ''
    key_index = 0
    for char in text:
        # Si c'est une lettre
        if char.isalpha():
            shift = key_int[key_index % key_len]
            # On utilise la fonction chr() pour récupérer la lettre cryptée
            # en fonction de son code ASCII et de la casse du message original
            if char.isupper():
                crypted_char = chr(((ord(char) - 65) + shift) % 26 + 65)
            else:
                crypted_char = chr(((ord(char) - 97) + shift) % 26 + 97)
            key_index += 1
        else:
            crypted_char = char
        crypted_text += crypted_char
    return crypted_text


# On définit une fonction de decryptage de Vigenère

def vigenere_decrypte(text, key):
    '''
    Fonction de décryptage de Vigenère
    text (str) : message crypté
    key (str) : clé de décryptage à utiliser
    Retourne (str) : message décrypté
    '''

    key = key.upper()
    key = key.replace(' ', '')

    key_len = len(key)
    key_int = [ord(i) - 65 for i in key]
    text_int = [ord(i) for i in text]
    decrypted_text = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = key_int[key_index % key_len]
            # On utilise la fonction chr() pour récupérer la lettre originale
            # en fonction de son code ASCII et de la casse du message original
            if char.isupper():
                decrypted_char = chr(((ord(char) - 65) - shift) % 26 + 65)
            else:
                decrypted_char = chr(((ord(char) - 97) - shift) % 26 + 97)
            key_index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text


# On définit une fonction de géneration de clés RSA

def rsa_keygen(p, q):
    '''
    Fonction de génération de clés RSA
    p (int) : premier nombre premier
    q (int) : deuxième nombre premier
    Retourne (tuple) : clés publique et privée sous forme de tuple (e, n), (d, n)
    '''
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choisissez un entier e tel que e et phi(n) sont copremiers
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    # Calculer l'exposant secret d tel que d * e = 1 (mod phi(n))
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return (e, n), (d, n)

# On définit une fonction de cryptage de RSA

def rsa_crypte(text, e, n):
    '''
    Fonction de cryptage RSA
    text (str) : message à crypter
    e (int) : exposant de cryptage
    n (int) : module
    Retourne (list) : message crypté sous forme de liste de nombres
    '''
    # On calcule les codes ASCII de chaque lettre de text
    text_int = [ord(i) for i in text]
    # Calculs mathématiques
    encrypted_text = [pow(i, e, n) for i in text_int]
    return encrypted_text

# On définit une fonction de decryptage de RSA

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

# Ce code permet de créer une interface pour crypter et décrypter un message en utilisant 
# différents algorithmes de chiffrement. 
# L'utilisateur peut sélectionner l'algorithme de son choix dans un menu déroulant 
# et entrer le message à crypter ou décrypter dans un champ de texte.

st.sidebar.header("Cryptage/décryptage du message")

st.sidebar.info('Le chiffre de César consiste à décaler chaque lettre du message de N positions dans l\'alphabet')
st.sidebar.info('Le chiffre de Vigenère consiste à utiliser une clé pour crypter le message avec le chiffre de César')
st.sidebar.info('RSA est un algorithme de cryptage asymétrique qui utilise une clé publique et une clé privée')

algorithm = st.sidebar.selectbox("Algorithme", ["César", "Vigenère", "RSA"])

text = st.sidebar.text_input("Message")

# Pour l'algorithme de César, l'utilisateur doit également entrer un décalage. 
if algorithm == "César":
    dec = st.sidebar.number_input("Décalage", min_value=0, max_value=25)

# Pour l'algorithme de Vigenère, il doit entrer une clé. 
elif algorithm == "Vigenère":
    key = st.sidebar.text_input("Clé")

# Pour l'algorithme RSA, il doit entrer deux nombres premiers.
elif algorithm == "RSA":
    p = st.sidebar.number_input("Nombre premier p", min_value=2, max_value=1000)
    q = st.sidebar.number_input("Nombre premier q", min_value=2, max_value=1000)
    # Generate the keys
    public_key, private_key = rsa_keygen(p, q)


# En cliquant sur les boutons "Crypter" ou "Décrypter", le message est transformé en utilisant l'algorithme sélectionné et 
# en utilisant les paramètres spécifiés par l'utilisateur. 

if st.sidebar.button("Crypter"):
    if algorithm == "César":
        crypte = cesar_crypte(text, dec)
    elif algorithm == "Vigenère":
        crypte = vigenere_crypte(text, key)
    elif algorithm == "RSA":
        crypte = rsa_crypte(text, *public_key)
    st.success(crypte, icon=None)

if st.sidebar.button("Décrypter"):
    if algorithm == "César":
        decrypte = cesar_decrypte(text, dec)
    elif algorithm == "Vigenère":
        decrypte = vigenere_decrypte(text, key)
    elif algorithm == "RSA":
        decrypte = rsa_decrypte(text, *private_key)
    st.success(decrypte, icon=None)
