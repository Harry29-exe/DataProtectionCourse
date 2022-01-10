import time

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def xor64(a, b):
    block = bytearray(a)
    for j in range(8):
        block[j] = a[j] ^ b[j]
    return bytes(block)


def encrypt_CTR_serial(key, nonce, plain_text):
    cipher_text = bytearray(plain_text)
    des = DES.new(key, DES.MODE_ECB)
    for i in range(no_blocks):
        offset = i * block_size
        nonce_counter = nonce + i.to_bytes(4, byteorder='big')
        encrypted = des.encrypt(nonce_counter)

        block = plain_text[offset:offset+block_size]
        cipher_text[offset:offset+block_size] = xor64(encrypted, block)

    return bytes(cipher_text)


def decrypt_CTR_serial(key, nonce, cipher_text):
    plain_text = bytearray(cipher_text)
    des = DES.new(key, DES.MODE_ECB)
    for i in range(no_blocks):
        nonce_counter = nonce + i.to_bytes(4, byteorder='big')

        encrypted = des.encrypt(nonce_counter)
        offset = i * block_size
        block = cipher_text[offset:offset+block_size]
        plain_text[offset:offset+block_size] = xor64(encrypted, block)

    return bytes(plain_text)


plain_text = b"alamakot"*100000
nonce = b"1234"
key = b"haslo123"
block_size = 8
no_blocks = int(len(plain_text) / block_size)

start_time = time.time()
cipher_text = encrypt_CTR_serial(key, nonce, plain_text)
print('CRT Encrypt time serial: ', (time.time() - start_time))
print('...', cipher_text[-15:-1])

start_time = time.time()
decrypted = decrypt_CTR_serial(key, nonce, cipher_text)
print('CRT Decrypt time serial: ', (time.time() - start_time))
print('...', decrypted[-15:-1])
print('...', decrypted[0:16])


with open('ciphertext', 'wb') as f:
    f.write(cipher_text)

with open('nonce', 'wb') as f:
    f.write(nonce)


