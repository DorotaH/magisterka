import math

n = int(input())
arr = list(map(int, input().split()))

min_lcm = float("inf")
min_i = -1
min_j = -1
for i in range(n):
    for j in range(1 + i, n):
        lcm = abs(arr[j] * arr[i]) // math.gcd(arr[i], arr[j])
        if min_lcm > lcm:
            min_lcm = lcm
            min_i, min_j = i + 1, j + 1

print(min_i, min_j)
