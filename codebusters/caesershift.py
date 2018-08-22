import random
import getletternumber
import letterfrequencychart
alphabet = "abcdefghijklmnopqrstuvwxyz"

def make_shift(message):
    shift = random.randint(1, 25)
    new_alphabet = ""
    ciphertext = ""
    message = message.lower()
    for letter in alphabet:
        new_alphabet = new_alphabet + alphabet[shift%26]
        shift += 1
    for le in message:
        x = getletternumber.get_letter_value(le,alphabet)
        try:
            ciphertext = ciphertext + new_alphabet[x]
        except TypeError:
            ciphertext = ciphertext + x
    print (ciphertext)
    print (letterfrequencychart.frequency_chart(ciphertext))
    return message + " \nAlphabet used: " + new_alphabet
