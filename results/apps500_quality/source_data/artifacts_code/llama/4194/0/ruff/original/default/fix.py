import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
n_days = N
hangout_days = 0
i = 0
for days in A:
    if n_days < days:
        print(-1)
        break
    n_days -= days
    hangout_days += n_days
    i += 1
else:
    print(hangout_days)
