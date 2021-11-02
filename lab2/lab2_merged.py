import string
import numpy as np

from math import log2

from Crypto.Cipher import ARC4


def calc_prob(s):
    prob = np.zeros(256)
    for ch in s:
        prob[ch] += 1

    return prob / len(s)


def calc_entropy(prob):
    H = 0.0
    for i in range(256):
        if prob[i] != 0:
            H -= prob[i] * log2(prob[i])

    return H


def check_password(passw, encodedText):
    pass_sum = ''.join(passw)
    password_bytes = bytes(pass_sum, "utf-8")

    cypher = ARC4.new(password_bytes)
    decrypted_text = cypher.decrypt(encodedText)
    if calc_entropy(calc_prob(decrypted_text)) < 7.0:
        print(password_bytes)
        print(decrypted_text)
        return True


encodedText1 = open("crypto.rc4", "rb").read()
encodedText2 = open("crypto2.rc4", "rb").read()
allCharacters = string.ascii_lowercase
password = ['a', 'a', 'a']
ARC4.key_size = range(1, 256)

password_found = False
for password[0] in allCharacters:
    for password[1] in allCharacters:
        for password[2] in allCharacters:
            if check_password(password, encodedText1):
                password_found = True
    if password_found:
        break

password_found = False
for password[0] in allCharacters:
    for password[1] in allCharacters:
        for password[2] in allCharacters:
            if check_password(password, encodedText2):
                password_found = True
    if password_found:
        break


import string
import numpy as np

from math import log2

from Crypto.Cipher import ARC4


def calc_prob(s):
    prob = np.zeros(256)
    for ch in s:
        prob[ch] += 1

    return prob / len(s)


def calc_entropy(prob):
    H = 0.0
    for i in range(256):
        if prob[i] != 0:
            H -= prob[i] * log2(prob[i])

    return H


def check_password(passw, encodedText):
    pass_sum = ''.join(passw)
    password_bytes = bytes(pass_sum, "utf-8")

    cypher = ARC4.new(password_bytes)
    decrypted_text = cypher.decrypt(encodedText)
    if calc_entropy(calc_prob(decrypted_text)) < 7.0:
        print(password_bytes)
        print(decrypted_text)
        return True


encodedText1 = open("crypto.rc4", "rb").read()
encodedText2 = open("crypto2.rc4", "rb").read()
allCharacters = string.ascii_lowercase
password = ['a', 'a', 'a']
ARC4.key_size = range(1, 256)

password_found = False
for password[0] in allCharacters:
    for password[1] in allCharacters:
        for password[2] in allCharacters:
            if check_password(password, encodedText1):
                password_found = True
    if password_found:
        break

password_found = False
for password[0] in allCharacters:
    for password[1] in allCharacters:
        for password[2] in allCharacters:
            if check_password(password, encodedText2):
                password_found = True
    if password_found:
        break

