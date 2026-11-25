n, k = map(int, input().split())
for x in range(k, n * k+k):
    if  (x // k) * (x % k) == n:
        print(x)
        break