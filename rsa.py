from math import sqrt
import random
ascii = "097 098 099 100 101 102 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122"
alphabet = "abcdefghijklmnopqrstuvwxyz"

# took this lcm code from online, credit to: https://www.w3resource.com/python-exercises/python-basic-exercise-32.php
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

# finds primes
def is_prime(number):
    if number>1:
        for u in range(2,round(sqrt(number))+1):
            if number%u == 0:
                return False
        else:
            pass
    else:
        print("bro u high?")

    return True

# code from : https://www.w3resource.com/python-exercises/python-basic-exercise-31.php
def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

def make_rsa(message):

    p = random.randint(2, 15)
    q = random.randint(2, 15)

    while is_prime(p) == False:
        p = random.randint(2,100)

    while is_prime(q) == False:
        q = random.randint(2,100)
    n = p*q
    l = lcm(p-1, q-1)
    possible_e = []
    for j in range(2, l):
        if gcd(l,j) == 1 and j < 8:
            possible_e.append(j)
        else:
            pass
    e = possible_e[random.randint(0, len(possible_e)-1)]
    '''for p in range(1,l):
        if (e*p)%l == 1:
            d = p
        else:
            pass (Since we aren't decoding, we don't need d)'''
    plain_numbers = []
    message = message.lower()
    finalmessage = ""
    og_num = 0

    # puts the number in ascii
    for le in message:
        if le in alphabet:
            og_num = alphabet.find(le)
            plain_numbers.append(og_num)
        else:
            pass
    for i in range(0, len(plain_numbers)):
        try:
            x = (plain_numbers[i])*4 - 4
            finalmessage = finalmessage + ascii[x:x+3]
        except TypeError:
            print("Uh oh, something went wrong!")
    finalmessage = int(finalmessage)
    encoded = (finalmessage ** e)%n
    print(finalmessage)
    print ("e: "+ str(e))
    print ("n: "+ str(n))
    return [message + "\n e: " + str(e) + "\n n: " + str(n), encoded]
