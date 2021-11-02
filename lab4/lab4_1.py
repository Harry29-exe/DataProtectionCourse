import time
import passlib.hash
from Crypto.Random import get_random_bytes

random_bytes = "skjgkhbsdkdgjhdsbguisdalbglkjs"
times_executed = pow(10, 2)

start_apr_md5 = time.time()
for i in range(times_executed):
    passlib.hash.apr_md5_crypt.hash(random_bytes)

time_apr_md5 = start_apr_md5 - start_apr_md5

start_bcrypt = time.time()
for i in range(times_executed):
    # random_bytes = get_random_bytes(16)
    passlib.hash.bcrypt.using(rounds=12).hash(random_bytes)

time_bcrypt = time.time() - start_bcrypt

print("Apr_md5 " + str(time_apr_md5))
print("BCrypt(12 rounds)  " + str(time_bcrypt))
