import time

time1 = time.time()
# //////////////////////


def get_primes(n):
    sieve = [True] * n
    sieve[:2] = [False, False]
    primes = []
    for prime, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        primes.append(prime)
        for not_prime in range(prime * prime, n, prime):
            sieve[not_prime] = False
    return primes


number_max = 2 * 10 ** 6
print(sum(get_primes(number_max)))

# //////////////////////
time2 = time.time()
print(f"{(time2 - time1) * 1000} ms")
