import math

p, y = map(int, input().split())

for i in range(int(math.sqrt(y)), 0, -1):
    if  i >= p and  y // i <= p:
        break
else:
    i=0

print(i if  i > 1 else -1)