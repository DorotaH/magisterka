for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    a.sort()
    y = a[0]
    for i in range(1, 1 + n // 2):
        print(a[i], y)
