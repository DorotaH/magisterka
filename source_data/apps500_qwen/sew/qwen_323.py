n = int(input())
if not n % 10 == 0:
    print(n + (10 - n % 10))
else:
    print(n)