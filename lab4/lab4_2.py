import hashlib

import passlib.hash
from Crypto.Random import get_random_bytes

checked_file = {}
full_hashes = {}

while True:
    random_bytes = get_random_bytes(512)
    sha224 = hashlib.sha224()
    sha224.update(random_bytes)
    bytes_hash = sha224.hexdigest()

    if checked_file.get(bytes_hash[:32]):
        file = checked_file.get(bytes_hash[:32])
        full_hash = full_hashes.get(file)
        print("For files:")
        print(file)
        print("and")
        print(random_bytes)
        print("first 32 bites of hash are identical: " + bytes_hash[:32])
        print("Full hash for first file: " + full_hash)
        print("Full hash for second file: " + bytes_hash)
        break
    else:
        checked_file[bytes_hash[:32]] = random_bytes
        full_hashes[random_bytes] = bytes_hash
