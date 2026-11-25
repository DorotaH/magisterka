import math
import sys

r = int(input())

if  r<3:
    print("NO")
    sys.exit()

x = int(math.sqrt(r - 1))
if not x * (x + 1) == r - 1:
    print("NO")
else:
    y = (r - x * x - x - 1) // 2
    if y > 0:
        print(x, y)
    else:
        print("NO")