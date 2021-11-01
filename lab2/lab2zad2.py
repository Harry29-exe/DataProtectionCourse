import string

import matplotlib.pyplot as plt
import numpy as np

s = str(open("1918_1.3_sample.txt", "rb").read())


def split(word):
    return [char for char in word]


n = 3
ascii_small_min = 97
ascii_small_max = 122
ascii_small_len = 122 - 96
ascii_big_min = 65
ascii_big_max = 90
ascii_big_len = 90 - 64
valid_chars = split(string.ascii_lowercase + string.ascii_uppercase)


def move(string, n):
    new_s = ""
    for c in string:
        if ascii_small_min <= ord(c) <= ascii_small_max:
            new_s += chr((ord(c) + n - ascii_small_min) % ascii_small_len + ascii_small_min)
        elif ascii_big_min <= ord(c) <= ascii_big_max:
            new_s += chr((ord(c) + n - ascii_big_min) % ascii_big_len + ascii_big_min)
        else:
            new_s += c

    return new_s


def count_bytes(text):
    count = np.zeros(len(valid_chars))
    for c in text:
        if c in string.ascii_lowercase:
            count[ord(c) - ascii_small_min] += 1
        elif c in string.ascii_uppercase:
            count[ord(c) - ascii_big_min + ascii_small_len] += 1

    return count


def encode_and_show_diagram(s, title):
    encoded = move(s, n)
    encoded_count = count_bytes(encoded)
    text_count = count_bytes(s)

    print(s)
    print(encoded)

    plt.title(title)
    plt.bar(valid_chars, encoded_count)
    plt.bar(valid_chars, text_count)
    plt.show()


encode_and_show_diagram(s, "PL")
s = str(open("CUP2.txt", "rb").read())
encode_and_show_diagram(s, "ENG")
