n, x = int(input()), int(input())

if not n % 2 == 0:
    print((x - 1) % 3)
else:
    print((x + 1) % 3)
