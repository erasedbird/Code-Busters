
def get_letter_value(plaintext,alphabet):
    if plaintext in alphabet:
        og_num = alphabet.find(plaintext)
    else:
        og_num = plaintext
    return og_num