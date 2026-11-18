n = int(input())
if 5 <= n:
    print(n)
    for i in range(1, 1 + n, 2):
        print(i, end=' ')
    for i in range(2, 1 + n, 2):
        print(i, end=' ')
elif n == 4:
    print(4)
    print(3, 1, 4, 2)
elif n == 3:
    print(2)
    print(1, 3)
else:
    print(1)
    print(1)