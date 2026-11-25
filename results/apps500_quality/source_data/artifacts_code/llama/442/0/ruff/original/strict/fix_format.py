import math
import sys

r = int(input())

if r < 3:
    print("NO")
    sys.exit()

x = int(math.sqrt(r - 1))
if x * (x + 1) == r - 1:
    y = (r - x * x - x - 1) // 2
    if y > 0:
        print(x, y)
    else:
        print("NO")
else:
    print("NO")
