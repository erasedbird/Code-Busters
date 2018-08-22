import random
alphabet = "abcdefghijklmnopqrstuvwxyz"

def make_mono_sub(message):
    ciphertext = ""
    new_alphabet = ""
    message = message.lower()
    random_letter = random.randint(0,25)
    while len(new_alphabet) < 26:
        if alphabet[random_letter] not in new_alphabet:
            new_alphabet = new_alphabet + alphabet[random_letter]
            random_letter = random.randint(0, 25)
        else:
            random_letter = random.randint(0,25)
    for le in message:
        if le in alphabet:
            messagenum = alphabet.find(le)
            ciphertext = ciphertext + new_alphabet[messagenum]
        else:
            ciphertext = ciphertext + le
    print (ciphertext)
    return message + " \nAlphabet used: " + new_alphabet
