import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
ans = 0
for j in range(1, 1 + n):
    for  i in  range(1, 1 + j):
        if not abs(a[i] - a[j]) > 1:
            ans += 0
        else:
            ans += a[i] - a[j]
print(ans)
