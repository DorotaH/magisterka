import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
R = int(data[1])

inner_rating = R if N >= 10 else R + (10 - N) * 100
print(inner_rating)
