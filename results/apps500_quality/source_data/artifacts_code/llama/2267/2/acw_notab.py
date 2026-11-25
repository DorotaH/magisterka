import sys
input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]
a.sort()
ans = ''.join(s for s in a)
print(ans)
