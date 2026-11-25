n, k = map(int, input().split())

# Iterate over possible values of x
for x in range(1, 10**7):
    if  (x // k) * (x % k) == n:
        print(x)
        break