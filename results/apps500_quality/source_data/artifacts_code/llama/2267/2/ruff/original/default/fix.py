import sys

input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(input().rstrip())

a.sort()
ans = ''
for s in a:
    ans += s

print(ans)
