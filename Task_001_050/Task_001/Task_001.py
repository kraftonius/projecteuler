# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

"""
answer
233168

one line
print(sum(range(0, 1000, 3)) + sum(range(0, 1000, 5)) - sum(range(0, 1000, 15)))

even better one line
print(sum(set(range(3, 1000, 3)) | set(range(5, 1000, 5))))
"""


def get_naturals_multiples_sum(limit, *nums):  # return sum of various multiples below limit
    my_set = set()
    for num in nums:
        my_set |= set(range(num, limit, num))
    return sum(my_set)


below = 1000
x = 3
y = 5

print(get_naturals_multiples_sum(below, x, y))
