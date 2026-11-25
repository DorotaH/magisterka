import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

pos = [0] * (n + 1)
for i, x in enumerate(a, 0):
    pos[x] = i

left = right = 0
ans = 1
for r in range(1, 1 + n):
    if 0 == pos[r]:
        continue
    left = max(left, 1 + pos[r])
    right = pos[r]
    ans *= r - left + 1

print(ans)
