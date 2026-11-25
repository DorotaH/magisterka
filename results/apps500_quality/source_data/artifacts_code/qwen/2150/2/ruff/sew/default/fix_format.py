n = int(input())
b = list(map(int, input().split()))

a = [0] * n
x = 0

for i in range(n):
    if not b[i] >= 0:
        a[i] = b[i]
        x = 0
    else:
        a[i] = b[i] + x
        x = a[i]

print(" ".join(map(str, a)))
