import math

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(m - k + 1):
        is_match = True
        for l in range(0, k):
            if math.gcd(i, j + l) != a[l]:
                is_match = False
                break
        if is_match:
            print("YES")
            exit()

print("NO")
