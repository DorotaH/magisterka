import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K, p = int(data[1]), list(map(int, data[2:]))

p.sort()
min_price = sum(p[:K], 0)

print(min_price)