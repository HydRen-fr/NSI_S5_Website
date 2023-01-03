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

def gcd(a, b):
    # Calculate the gcd of a and b using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b):
    # Calculate the inverse of a modulo b using the extended Euclidean algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

def is_prime(n):
    # Test if a number is prime using the Miller-Rabin primality test
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(5):
        a = randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    
def generate_keypair(p, q):
    # Generate a public and private key using p and q
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal.')
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randrange(1, phi)
        g = gcd(e, phi)
    d = extended_euclidean_algorithm(e, phi)[1]
    # Make sure d is positive
    if d < 0:
        d += phi
    # Return public and private keypair
    return ((e, n), (d, n))

def rsa_crypte(pk, text):
    # Encrypt the text using the public key
    key, n = pk
    text = [(ord(char) ** key) % n for char in text]
    return text

def rsa_decrypte(pk, text):
    # Decrypt the text using the private key
    key, n = pk
    text = [chr((char ** key) % n) for char in text]
    return ''.join(text)



# CODE DU SITE

st.sidebar.header("Cryptage/décryptage du message")


algorithm = st.sidebar.selectbox("Algorithme", ["César", "Vigenère", "RSA"])
text = st.sidebar.text_input("Message")


if algorithm == "César":
    dec = st.sidebar.number_input("Décalage", min_value=0, max_value=25)

elif algorithm == "Vigenère":
    key = st.sidebar.text_input("Clé")

elif algorithm == "RSA":
    st.sidebar.header("Génération de la paire de clés")
    p = st.sidebar.number_input("Nombre premier p", min_value=0)
    q = st.sidebar.number_input("Nombre premier q", min_value=0)
    public, private = generate_keypair(p, q)
    st.sidebar.header("Clés")
    st.sidebar.markdown(f'Clé publique: {public}')
    st.sidebar.markdown(f'Clé privée: {private}')

if st.sidebar.button("Crypter"):
    if algorithm == "César":
        crypte = cesar_crypte(text, dec)

    elif algorithm == "Vigenère":
        crypte = vigenere_crypte(text, key)
        
    elif algorithm == "RSA":
        crypte = rsa_crypte(public, text)
    st.success("Message crypté : {}".format(crypte))


if st.sidebar.button("Décrypter"):
    if algorithm == "César":
        decrypte = cesar_decrypte(text, dec)

    elif algorithm == "Vigenère":
        decrypte = vigenere_decrypte(text, key)
        
    elif algorithm == "RSA":
        decrypte = rsa_decrypte(private, text)
    st.success("Message décrypté : {}".format(decrypte))
