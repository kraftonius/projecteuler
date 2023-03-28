# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that
# is evenly divisible by all of the numbers from 1 to 20?

import numpy as np

def get_primes(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    primes = []
    for prime, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        primes.append(prime)
        for not_prime in range(prime * prime, n + 1, prime):
            sieve[not_prime] = False
    return primes


def get_raw_pow_list(n):
    list_pow = [[]]
    my_list = []
    for ind in range(2, n + 1):
        my_list.append(ind)
    for i in my_list:
        for j in get_primes(n):
            count = 0
            while i % j == 0:
                i /= j
                count += 1
                if count > 0:
                    list_pow.append([j, count])
    list_pow.remove([])
    return list_pow


def get_pow_list(n):
    my_pow_list = [[]]
    pow_raw = get_raw_pow_list(n)
    for i in get_primes(n):
        temp_list = [[]]
        for j in range(len(pow_raw)):
            if i == pow_raw[j][0]:
                temp_list.append(pow_raw[j])
        temp_list.remove([])
        max_list = temp_list[0]
        for k in range(len(temp_list)):
            if temp_list[k][1] > max_list[1]:
                max_list = temp_list[k]
        my_pow_list.append(max_list)
    my_pow_list.remove([])
    return my_pow_list


def compute_pow_list(n):
    list_x = get_pow_list(n)
    prod = 1
    for i in range(len(list_x)):
        prod *= pow(list_x[i][0], list_x[i][1])
    return prod


num = 20
print(compute_pow_list(num))

"""
Answer:  232792560
"""