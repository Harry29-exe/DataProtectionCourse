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


def check_password(password):
    passSum = ''.join(password)
    passBytes = bytes(passSum, "utf-8")

    # hack!
    cypher = ARC4.new(passBytes)  # hack!
    decryptedText = cypher.decrypt(encodedText)
    if calc_entropy(calc_prob(decryptedText)) < 7.0:
        print(decryptedText)


encodedText = open("crypto.rc4", "rb").read()
allCharacters = string.ascii_lowercase
# + string.ascii_uppercase
password = ['a', 'a', 'a']
ARC4.key_size = range(1, 256)

for password[0] in allCharacters:

    check_password([password[0]])

for password[0] in allCharacters:
    for password[1] in allCharacters:
        check_password([password[0], password[1]])

for password[0] in allCharacters:
    for password[1] in allCharacters:
        for password[2] in allCharacters:
            check_password(password)

    print(password[0])
