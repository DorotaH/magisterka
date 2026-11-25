n = int(input())
if  n<10:
    print(n)
elif  n<100:
    print(9 + 2 * (n - 9))
elif  n<1000:
    print(9 + 2 * 90 + 3 * (n - 99))
else:
    print(9 + 2 * 90 + 3 * 900 + 4 * (n - 999))
