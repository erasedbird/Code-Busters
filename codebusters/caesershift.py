import random
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
        if le in alphabet:
            messagenum = alphabet.find(le)
            ciphertext = ciphertext + new_alphabet[messagenum]
        else:
            ciphertext = ciphertext + le
    print (ciphertext)
    return message + " \nAlphabet used: " + new_alphabet
