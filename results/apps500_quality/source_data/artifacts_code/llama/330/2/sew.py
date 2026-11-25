import math

p, y = map(int, input().split())

for x in range(p, 0, -1):
    if  all(y // x > 2 and  1 == (y // x) % 2 and  not  all(y // i for  i in  range(2, 1 + int(math.sqrt(y // x)), 2) if  0 == (y // x) % (y // i))):
        print(y)
        break
else:
    print(-1)