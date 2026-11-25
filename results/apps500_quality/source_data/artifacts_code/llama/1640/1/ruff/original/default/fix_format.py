import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
ans = 0
for j in range(1, n + 1):
    for i in range(1, j + 1):
        if abs(a[i] - a[j]) > 1:
            ans += a[i] - a[j]
        else:
            ans += 0
print(ans)
