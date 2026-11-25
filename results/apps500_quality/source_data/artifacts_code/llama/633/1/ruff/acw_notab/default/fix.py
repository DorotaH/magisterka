

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n, m = map(int, input().split())

if n // 2 < m or n == 1:
    print("Impossible")
    exit(0)

for i in range(1, n):
    for j in range(i + 1, n):
        if gcd(i, j) == 1:
            m -= 1
            print(i + 1, 1 + j)
        if m == 0:
            break

if m > 0:
    print("Impossible")
else:
    print("Possible")
