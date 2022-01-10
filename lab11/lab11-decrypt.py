import multiprocessing
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def xor64(a, b):
    block = bytearray(a)
    for j in range(8):
        block[j] = a[j] ^ b[j]
    return bytes(block)


def init(shared_data, output_data, block_size, key, nonce):
    multiprocessing.shared_data = shared_data
    multiprocessing.output_data = output_data
    multiprocessing.block_size = block_size
    multiprocessing.key = key
    multiprocessing.nonce = nonce


def mapper(blocks):
    cipher_text = multiprocessing.shared_data
    plain_text = multiprocessing.output_data
    block_size = multiprocessing.block_size
    nonce = multiprocessing.nonce
    des = DES.new(multiprocessing.key, DES.MODE_ECB)

    for i in blocks:
        nonce_counter = nonce + i.to_bytes(4, byteorder='big')

        encrypted = des.encrypt(nonce_counter)
        offset = i * block_size
        block = cipher_text[offset:offset+block_size]
        plain_text[offset:offset+block_size] = xor64(encrypted, block)
    return i

if __name__ == '__main__':
    key = b"haslo123"
    nonce = b"1234"
    block_size = 8
    cipher_text = open("ciphertext", "rb").read()
    no_blocks = int(len(cipher_text)/block_size)
    W = 4

    shared_data = multiprocessing.RawArray(ctypes.c_ubyte, cipher_text)
    output_data = multiprocessing.RawArray(ctypes.c_ubyte, cipher_text)
    blocks = [range(i, no_blocks, W) for i in range(W)]
    print(blocks)
    pool = multiprocessing.Pool(W, initializer=init, initargs=(shared_data, output_data, block_size, key, nonce))
    starttime = time.time()
    pool.map(mapper, blocks)
    print('ECB Decrypt time parallel: ', (time.time() - starttime))
    decrypted = bytes(output_data)
    print('...', decrypted[-15:-1])
    print('...', decrypted[0:16])
