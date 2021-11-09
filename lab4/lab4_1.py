import time
import passlib.hash
from Crypto.Random import get_random_bytes

random_bytes = "skjgkhbsdkdgjhdsbguisdalbglkjs"
times_executed_md5 = pow(10, 4)
times_executed_bcrypt = pow(10, 2)

start_apr_md5 = time.time()
for i in range(times_executed_md5):
    passlib.hash.apr_md5_crypt.hash(random_bytes)

time_apr_md5 = time.time() - start_apr_md5

start_bcrypt = time.time()
for i in range(times_executed_bcrypt):
    # random_bytes = get_random_bytes(16)
    passlib.hash.bcrypt.using(rounds=10).hash(random_bytes)

time_bcrypt = time.time() - start_bcrypt

# TODO jak działa bcypt rounds 2^x?
print("Average Apr_md5 " + str(time_apr_md5 / times_executed_md5))
print("Average BCrypt(10 rounds)  " + str(time_bcrypt / times_executed_bcrypt))
