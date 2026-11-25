import sys

input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]

a.sort()
ans = ''
for s in a:
    ans += s

print(ans)