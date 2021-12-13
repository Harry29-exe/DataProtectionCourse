from client import Client

c = Client("http://192.168.8.100:5000/")

from Crypto.PublicKey import RSA

keys = RSA.generate(2048)

privkey = keys
pubkey = keys.public_key()
pubkey_str = pubkey.export_key()

c.send_key(uid="kw", key=pubkey_str)

msg = "non encrypted message"
c.send_text_message(uid="wk", msg=msg)
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
msg_hash = SHA256.new(msg.encode())
sig = pkcs1_15.new(privkey).sign(msg_hash)
print(len(sig))
sig = b"".join([sig[:-2], b"aa"])
print(len(sig))
c.send_binary_message(uid="wk.sig", msg=sig)