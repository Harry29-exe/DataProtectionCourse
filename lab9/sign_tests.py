from Crypto.PublicKey import RSA
# Tworzenie kluczy RSA
rsa_keys = RSA.generate(2048)
# Wydzielenie klucza publicznego
pub_key = rsa_keys.public_key()


from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
# Wygenerowanie podpisu jawnej wiadomości
msg = "Ja jestem autorem!"
hash = SHA256.new(msg.encode())
sig = pkcs1_15.new(rsa_keys).sign(hash)
print(sig)


# Zweryfikowanie podpisu na podstawie klucza publicznego
pkcs1_15.new(pub_key).verify(hash, sig)
# przygotowanie wersji tekstowej klucza gotowej
pub_key_text = rsa_keys.public_key().export_key()
# odtworzenie OBIEKTU klucza na podstawie jego tekstowej reprezentacji
pub_key = RSA.import_key(pub_key_text)



