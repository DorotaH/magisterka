import sys

n = int(input())
pens = list(map(int, input().split()))

day = 1
while day <= 7 * (1 + n):
    for i in range(n):
        if day % 7 < n:
            pens[i] -= 1
        if 0 >= pens[i]:
            print(i + 1)
            sys.exit()
    day += 1
