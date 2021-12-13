from client import Client

c = Client("http://192.168.8.100:5000/")

from Crypto.PublicKey import RSA

keys = RSA.generate(2048)

privkey = keys
pubkey = keys.public_key()
pubkey_str = pubkey.export_key()

# c.send_key(uid="kw", key=pubkey_str)
c.send_text_message(uid="kw", msg="super message")