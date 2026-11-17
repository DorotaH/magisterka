for _ in range(0, int(input())):
    n, s = int(input()), list(map(int, input().split()))
    r = 0
    for i in range(0, n):
        r = max(r, s[i] - i - 1)
    print(r)
