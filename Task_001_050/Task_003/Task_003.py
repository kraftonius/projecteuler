# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import time

time1 = time.time()

def get_max_prime_divider(num):
    while num % 2 == 0:
        num //= 2
    div = 3
    while div * div <= num:
        while num % div == 0:
            num //= div
        div += 2
    if num > 1:
        return num
    else:
        return div - 1


# 600851475143
number = 60085147514312312312
max_prime_div = get_max_prime_divider(number)
print(max_prime_div)

time2 = time.time()
print(f"{(time2 - time1) * 1000} ms")

"""
Answer:  6857
"""
