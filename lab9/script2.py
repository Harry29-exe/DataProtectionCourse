import sys
key_owner = sys.argv[1]
print("owner: ", key_owner)
msg_receiver = sys.argv[2]
print("receiver: ", msg_receiver)

from client import Client
c = Client("http://192.168.8.100:5000/")

pubkey_str = c.get_key(uid=key_owner)
print("pubkey:", pubkey_str)
from Crypto.PublicKey import RSA
pubkey = RSA.import_key(pubkey_str)

msg = c.get_text_message(uid=msg_receiver)
print("msg:", msg)
msg_sig = c.get_binary_message(uid=(msg_receiver+".sig"))
print("msg_sig:",msg_sig)

from Crypto.Hash import SHA256
msg_hash = SHA256.new(msg.encode())

from Crypto.Signature import pkcs1_15
try:
    pkcs1_15.new(pubkey).verify(msg_hash, msg_sig)
    print("Message signature is valid")
except ValueError:
    print("WARNING: message signature is not valid")
