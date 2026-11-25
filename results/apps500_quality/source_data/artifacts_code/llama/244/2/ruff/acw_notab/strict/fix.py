n = int(input())
x = int(input())

if n % 2 == 0:
    print((1 + x) % 3)
else:
    print((x - 1) % 3)
