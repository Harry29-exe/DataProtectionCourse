import passlib.hash

we = passlib.hash.bcrypt.hash("haslo")
print(we)
we2 = passlib.hash.bcrypt.using(rouds = 15).hash("haslo")
