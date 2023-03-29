# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

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


sequence = 1000000
primes_list = (get_primes(sequence * 20))
print(primes_list[sequence - 1])
