n = int(input())
if 10 > n:
    print(n)
elif 100 > n:
    print(9 + 2 * (n - 9))
elif 1000 > n:
    print(9 + 2 * 90 + (n - 99) * 3)
else:
    print(9 + 2 * 90 + 900 * 3 + (n - 999) * 4)
