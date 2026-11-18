import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [0] * 4
for _ in range(0, N):
    x, y = map(int, input().split())
    x, y = x // 2, y // 2
    A[(x % 2) * 2 + y % 2] += 1

ans = 0
for i in range(0, 4):
    a = A[i]
    s = a * (a - 1) // 2
    ans += s * (a - 2) // 3
    for j in range(4):
        if j == i:
            continue
        b = A[j]
        ans += b * s
print(ans)
