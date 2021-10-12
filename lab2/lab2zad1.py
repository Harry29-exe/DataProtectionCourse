import string
import numpy as np

from math import log2

from Crypto.Cipher import ARC4


def calc_prob(s):
    prob = np.zeros(256)
    for c in s:
        prob[c] += 1

    return prob / len(s)


def calc_entropy(prob):
    H = 0.0
    for i in range(256):
        H -= prob[i] * log2(prob[i])

    return H


encodedText = open("crypto.rc4", "rb").read()
allCharacters = string.ascii_lowercase
                # + string.ascii_uppercase
password = ['a', 'a', 'a']
for a in allCharacters:
    for b in allCharacters:
        for c in allCharacters:
            passSum = ''.join(password)
            passBytes = bytes(passSum, "utf-8")

            ARC4.key_size = range(3, 256)
            # hack!
            cypher = ARC4.new(passBytes)  # hack!
            decryptedText = cypher.decrypt(encodedText)
            if calc_entropy(calc_prob(decryptedText)) < 7.0:
                print(decryptedText)

    print(a)
