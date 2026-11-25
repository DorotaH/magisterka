n = int(input())
if not n % 10 == 0:
    print(n - n % 10)
else:
    print(n)