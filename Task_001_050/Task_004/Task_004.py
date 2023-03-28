# A palindromic number reads the same both ways.
# The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


try:
    for i in range(999, 99, -1):
        n = i
        r_n = 0
        while n != 0:
            r_n = r_n * 10 + n % 10
            n //= 10
        pal = i * 1000 + r_n
        for j in range(999, 99, -1):
            if pal % j == 0 and pal / j <= 999:
                print(pal)
                raise StopIteration
except StopIteration:
    pass

"""
Answer:  906609
"""
