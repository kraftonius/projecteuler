# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# m > n
# a = k * (m ** 2 - n ** 2)
# b = k * (2 * m * n)
# c = k * (m ** 2 + n ** 2)

def get_abc_prod(abc_s):
    limit = int(pow(abc_sum, 1 / 2))
    for m in range(limit):
        for n in range(limit):
            if n >= m:
                break
            for k in range(limit):
                a = k * (m ** 2 - n ** 2)
                b = k * (2 * m * n)
                c = k * (m ** 2 + n ** 2)
                if a + b + c == abc_s:
                    return a * b * c

abc_sum = 1000
print(get_abc_prod(abc_sum))

"""
Answer: 31875000
"""



