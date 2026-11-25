import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
p = list(map(int, data[2:]))

p.sort()
min_price = sum(p[:K])

print(min_price)
