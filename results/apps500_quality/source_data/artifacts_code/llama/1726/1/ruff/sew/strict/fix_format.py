import sys

n, t = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

total_time = 0
for i in range(n):
    total_time += a[i]
    if t - total_time < 0:
        print(1 + i)
        break
else:
    print(n)
