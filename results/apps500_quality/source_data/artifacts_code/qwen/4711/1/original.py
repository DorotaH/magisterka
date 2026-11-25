import sys
input = sys.stdin.read
data = input().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])

bells = [a, b, c]
bells.sort()

min_price = min(a + b, a + c, b + c)

print(min_price)
