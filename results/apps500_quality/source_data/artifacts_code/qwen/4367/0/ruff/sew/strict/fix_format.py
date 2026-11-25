import sys

input = sys.stdin.read
data = input().split()

N, R = int(data[0]), int(data[1])

if N >= 10:
    inner_rating = R
else:
    inner_rating = R + 100 * (10 - N)

print(inner_rating)
