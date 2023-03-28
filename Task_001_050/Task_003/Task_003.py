# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


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


number = 600851475143
max_prime_div = get_max_prime_divider(number)
print(max_prime_div)

"""
Answer:  6857
"""
