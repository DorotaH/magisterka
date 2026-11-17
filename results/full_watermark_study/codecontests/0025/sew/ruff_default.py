for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    mx = -pow(10, 9)
    for i in range(n - 1):
        mx = max(mx, l[i] * l[i + 1])
    print(mx)
