"""
Name: substitution_cipher.py
Author: Nathaniel Grundmann
Description: Generates a Substitution Cypher
"""

from random import shuffle

def create_cipher():
    alpha_num_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                      'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', ' ', '.']
    alpha_num_values = alpha_num_keys.copy()
    shuffle(alpha_num_values)
    cipher = dict(zip(alpha_num_keys, alpha_num_values))
    return cipher
    
def input_message():
    message = input("Please type your message: ")
    return message

def encode_message(cipher, message):
    encoded_message = []
    for char in message:
        encoded_message.append(cipher[char])
    return encoded_message

cipher = create_cipher()
message = input_message()
encoded_message = encode_message(cipher, message)
print(encoded_message)
