# Hi! Welcome to the Code Busters Test by me! Feel free to add more things to plaintext or vingerecodewords (but make sure vingere code words only have letters!).
print ("Hi! Welcome to the Code Busters Test! Feel free to add more stuff to plaintext, vingerecodewords, or rsaplain.")
print ("Remember to set a timer for 50 minutes! (If you want a timed question, pick one of the monoalpabetic subsitution and time yourself!)")
print ("A key will be available at the end whenever you want.")

# imports all the cipher functions

import Affinecipher
import Vingerecipher
import Monoalphabetic
import caesershift
import Baconcipher
import random
import rsa

# Opens the files containing the plaintext and the vingere codewords and moves them onto two lists

with open("plaintext.txt","r") as plainfile:
    plainlines = plainfile.readlines()

with open("vingerecodewords.txt","r") as vingerestuff:
    vingerelines = vingerestuff.readlines()

with open("rsaplain.txt","r") as rsastuff:
    rsalines = rsastuff.readlines()

# checks if the entered values are integers


def check_int(number):
    x = 0
    while x == 0:
        try:
            number = int(number)
            if number < 0:
                print("You can't have negative ciphers!")
                number = input("Enter a positive number. \n")
            elif number > len(plainlines)/5:
                number = input("Your number was too big! Try again. \n")
            else:
                print("You will get %s cipher(s)." % number)
                break
        except ValueError:
            print("You didn't enter a number, try again.")
            number = input("Enter a number: \n")
    return number

# asks for number of ciphers


number_of_af = input("How many affine ciphers do you want? \n")
number_of_af = check_int(number_of_af)
number_of_vc = input("How many vingere ciphers do you want? (encode or decode with key) \n")
number_of_vc = check_int(number_of_vc)
number_of_ms = input("How many monoalphabetic substitution ciphers do you want? \n")
number_of_ms = check_int(number_of_ms)
number_of_cs = input("How many caesar shift ciphers do you want? \n")
number_of_cs = check_int(number_of_cs)
number_of_bc = input("How many Baconian ciphers do you want? \n")
number_of_bc = check_int(number_of_bc)
number_of_rsa = input("How many rsa do you want? (Note: these require heavy use of calculators.)\n")
number_of_rsa = check_int(number_of_rsa)

# picks the right number of plaintexts/vingere codewords for the cipher

total_ciphers = int(number_of_af) + int(number_of_ms) + int(number_of_vc) + int(number_of_cs) + int(number_of_bc)
print ("You are getting " + str(total_ciphers) + " questions.")
selected_plain = []
selected_vingere = []
selected_rsa = []
for i in range(0, int(total_ciphers)):
    ruv = random.randint(-1, len(plainlines)-1)
    popped = plainlines.pop(ruv)
    selected_plain.append(popped)
for i in range(0, int(number_of_vc)):
    ruv = random.randint(-1, len(vingerelines)-1)
    popped = vingerelines.pop(ruv)
    selected_vingere.append(popped)
for i in range(0, int(number_of_rsa)):
    ruv = random.randint(-1, len(rsalines)-1)
    popped = rsalines.pop(ruv)
    selected_rsa.append(popped)

#removes \n

final_selected_plain = []
for things in selected_plain:
    things = things.replace("\n", "")
    final_selected_plain.append(things)
# print (final_selected_plain)
final_selected_vingere = []
for things in selected_vingere:
    things = things.replace("\n", "")
    final_selected_vingere.append(things)
# print (final_selected_vingere)
final_selected_rsa = []
for things in selected_rsa:
    things = things.replace("\n", "")
    final_selected_rsa.append(things)

# asks for how many of each question you want, and also generate a key
key = []

for i in range(0, number_of_af):
    print("\n Affine Question "+ str(i+1))
    x = Affinecipher.make_affine_cipher(final_selected_plain[i])
    key.append(str(i+1) + "." + x)
for i in range(number_of_af, number_of_af + number_of_vc):
    print("\n Vingere Question " + str(i+1))
    x = Vingerecipher.make_vingere(final_selected_plain[i], final_selected_vingere[i-number_of_af])
    key.append(str(i+1) + "." + x)

for i in range(number_of_af + number_of_vc, number_of_af + number_of_vc + number_of_ms):
    print("\n Monoalphabetic Subsitution Question " + str(i+1))
    x = Monoalphabetic.make_mono_sub(final_selected_plain[i])
    key.append(str(i+1) + "." + x)

for i in range(number_of_af + number_of_vc + number_of_ms, number_of_af + number_of_vc + number_of_ms + number_of_cs):
    print("\n Caesar Shift Question " + str(i+1))
    x = caesershift.make_shift(final_selected_plain[i])
    key.append(str(i+1) + "." + x)

for i in range(number_of_af + number_of_vc + number_of_ms + number_of_cs, number_of_af + number_of_vc + number_of_ms + number_of_cs + number_of_bc):
    print("\n Baconian Cipher Question " + str(i+1))
    x = Baconcipher.make_bacon(final_selected_plain[i])
    key.append(str(i+1) + "." + x)
for i in range(0,number_of_rsa):
    print("\n RSA Question "+ str(i+1+number_of_af + number_of_vc + number_of_ms + number_of_cs + number_of_bc))
    x = rsa.make_rsa(final_selected_rsa[i])
    key.append(str(i+1+number_of_af + number_of_vc + number_of_ms + number_of_cs + number_of_bc)+ "." + str(x))

# prints the key if there is one
if len(key) == 0:
    print("\nDon't blame me when you fail your Code Busters event!")
else:
    hi = input("\nType anything here when you want the key. \n")
    for items in range(0, len(key)):
        print(key[items])
print("\nThank you for taking my test!")
