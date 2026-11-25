import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

pos = [0] * (n + 1)
for i, x in enumerate(a):
    pos[x] = i

left = 0
right = 0
ans = 1
for r in range(1, n + 1):
    if pos[r] == 0:
        continue
    left = max(left, pos[r] + 1)
    right = pos[r]
    ans *= (r - left + 1)

print(ans)
