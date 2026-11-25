n, k = map(int, input().split())
for x in range(k, k * n + k):
    if (x // k) * (x % k) == n:
        print(x)
        break
