# The sum of the squares of the first ten natural numbers is,
# 1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+3)**2 = 3025
# Hence the difference between the sum of the squares of
# the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

n = 100

# one line
# print(((n * (n + 1) // 2) ** 2) - (n * (n + 1) * (2 * n + 1)) // 6)

sum_q1 = sum_q2 = 0
for ind in range(n + 1):
    sum_q1 += ind * ind
    sum_q2 += ind
res = sum_q2 * sum_q2 - sum_q1
print(res)

"""
Answer: 25164150
"""
