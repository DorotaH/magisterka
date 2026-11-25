import sys

input = sys.stdin.read
data = input().split()

n, k = int(data[0]), int(data[1])

if not k == 0:
    multiplier = 10**k
    if n % multiplier == 0:
        print(n)
    else:
        print((n // multiplier + 1) * multiplier)
else:
    print(n)