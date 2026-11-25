n = int(input())
if n % 10 != 0:
    if 5 > n % 10:
        n -= n % 10
    else:
        n += 10 - n % 10
print(n)
