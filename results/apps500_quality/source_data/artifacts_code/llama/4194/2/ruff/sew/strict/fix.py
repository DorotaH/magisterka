import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

hangout_days = days = 0

for i in range(m):
    if  days + a[i] > n:
        print(-1)
        sys.exit()

    days += a[i]
    hangout_days += n - days

print(hangout_days)
