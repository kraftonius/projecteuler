# Each new term in the Fibonacci sequence
# is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.


def even_fibonacci(max_num):
    fib_list = [1, 2]
    i = 2
    while fib_list[i - 1] + fib_list[i - 2] <= max_num:
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        i += 1
    even_fib = []
    for j in fib_list:
        if j % 2 == 0:
            even_fib.append(j)
    return even_fib


maximum = 4000000
my_fib_list = even_fibonacci(maximum)
print(my_fib_list)
print(sum(my_fib_list))

"""
Answer:  4613732
"""