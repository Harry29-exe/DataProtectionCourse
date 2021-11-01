import string
from math import log2

import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import BMPcrypt


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


def decrypt_full(input_filename, mode, key, iv=None):
    img_in = open(input_filename, "rb")
    data = img_in.read()
    if mode == "ECB":
        aes = AES.new(key=key, mode=AES.MODE_ECB)
    else:
        aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

    decrypted_data = aes.decrypt(BMPcrypt.nullpadding(data))

    in_name_parts = input_filename.split('.')
    in_name = in_name_parts[0].split('_')
    # mode = in_name[len(in_name) - 2]

    output_filename = "decrypted.bmp"
    img_out = open(output_filename, "wb")
    img_out.write(decrypted_data)
    img_out.close()
    img_in.close()


path = "/home/kamil/PycharmProjects/DataProtectionCourse/lab3/"
filename = "security_ECB_encrypted.bmp"

possibleValue = string.ascii_lowercase + string.digits
img_data = open(path + filename, "rb").read()
real_key = None
first_128_bits = ""
for i in possibleValue:
    key = ""
    for j in range(16):
        key += i
    key_bytes = bytes(key, 'ASCII')

    aes = AES.new(key=key_bytes, mode=AES.MODE_ECB)
    decrypted_data = aes.decrypt(BMPcrypt.nullpadding(img_data))
    if calc_entropy(calc_prob(decrypted_data[:14])) < 3:
        print(key)
        real_key = key_bytes
        first_128_bits = decrypted_data[:128]

# decrypt_full(path + filename, "ECB", real_key)


cbc_filename = "security_CBC_encrypted.bmp"
def decrypt_full_mod(input_filename, mode, key, first_128):
    img_in = open(input_filename, "rb")
    data = img_in.read()
    if mode == "ECB":
        aes = AES.new(key=key, mode=AES.MODE_ECB)
    else:
        aes = AES.new(key=key, mode=AES.MODE_CBC)

    decrypted_data = aes.decrypt(BMPcrypt.nullpadding(data))
    decrypted_data = first_128 + decrypted_data[128:]

    in_name_parts = input_filename.split('.')
    in_name = in_name_parts[0].split('_')
    # mode = in_name[len(in_name) - 2]

    output_filename = "decrypted.bmp"
    img_out = open(output_filename, "wb")
    img_out.write(decrypted_data)
    img_out.close()
    img_in.close()


decrypt_full_mod(path + cbc_filename, "CBC", real_key, first_128_bits)
# key = get_random_bytes(16)
# BMPcrypt.encrypt_full(path + 'demo24_copy.bmp', "ECB", key)
# print("success")
# decrypt_full(path + "demo24_copy_ECB_encrypted.bmp", "ECB", key)
