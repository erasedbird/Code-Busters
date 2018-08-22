import random
values_of_a = [3,5,7,9,11,15,17,19,21,25]
a = values_of_a[random.randint(0,9)]
b = random.randint(1,20)

alphabet = "abcdefghijklmnopqrstuvwxyz"

def make_affine_cipher(something):
    final_str = ""
    something = something.lower()
    for letter in something:
        if letter not in alphabet:
            final_str = final_str + letter
        else:
            og_number = alphabet.find(letter)
            cipher_letter = (og_number*a)+b
            final_str = final_str + alphabet[cipher_letter%26]
    # picks whether to encode or decode and returns the key
    x = random.randint(1,3)
    if x<2:
        print ("Decode: " + final_str)
        x = random.randint(0,3)
        # either prints first 4 letters or prints a and b
        if x<2:
            print ("The first four letters of the word are: " + something[:5])
        else:
            print("a:"+str(a))
            print("b:"+str(b))
        return something
    else:
        print("Encode: " + something)
        print ("a:"+str(a))
        print ("b:" +str(b))
        return final_str

