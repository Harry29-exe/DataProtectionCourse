s = "ala ma kota"
n = 3
ascii_min = 65
ascii_max = 122
ascii_length = ascii_max - ascii_min

def move(string, n):
    new_s = ""
    for i in range(len(string)):
        new_s += chr(
            (ord(string[i]) + n - ascii_min) % ascii_length + ascii_min
        )

    return new_s


new_s = move(s, n)
print(new_s)
n = -3
print(move(new_s, n))