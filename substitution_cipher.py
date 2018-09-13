"""
Name: substitution_cipher.py
Author: Nathaniel Grundmann
Description: Generates a Substitution Cypher
"""

from random import randint

def create_cipher():
    alpha_num_keys = ['a', 'b',  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    alpha_num_values = alpha_num_keys
    cipher = {}
    for char in alpha_num_keys:
        random_index = randint(0,(len(alpha_num_values)-1))
        cipher[char] = alpha_num_values.pop(random_index)
    return cipher

cipher = create_cipher()

print(cipher)
