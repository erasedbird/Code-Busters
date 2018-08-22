import random
import getletternumber
alphabet = "abcdefghijklmnopqrstuvwxyz"

def make_vingere(plaintext, keyword):
    key_numbers = []
    plain_numbers = []
    cipher_text = ""
    current_numb = 0
    vingere_num = 0
    plaintext = plaintext.lower()
    keyword = keyword.lower()

    # converts everything to numbers

    for letter in keyword:
        if letter in alphabet:
            x = getletternumber.get_letter_value(letter, alphabet)
            key_numbers.append(x)
        else:
            pass
    for le in plaintext:
        x = getletternumber.get_letter_value(le, alphabet)
        plain_numbers.append(x)

    # actually does the vingere thingy

    for values in plain_numbers:
        try:
            sum = key_numbers[vingere_num % len(key_numbers)] + plain_numbers[current_numb]
            cipher_text = cipher_text + alphabet[sum % 26]
            current_numb += 1
            vingere_num += 1
        except TypeError:
            cipher_text = cipher_text + plain_numbers[current_numb]
            current_numb += 1
    # randomly selects whether to have you endcode or decode it
    x = random.randint(1,3)
    if x < 2:
        print ("Decode: " + cipher_text)
        print("The keyword is " + keyword + ".")
        return(plaintext)
    else:
        print ("Encode: " + plaintext)
        print ("The keyword is " + keyword + ".")
        return cipher_text
