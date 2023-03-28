import time

time1 = time.time()
# //////////////////////

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



# //////////////////////
time2 = time.time()
print(f"{(time2 - time1) * 1000} ms")
