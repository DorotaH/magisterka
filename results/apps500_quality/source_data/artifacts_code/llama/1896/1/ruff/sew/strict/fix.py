import math

n = int(input())
if not n == 0:
    a = 2 * n + 1
    b = 6 * n
    c = math.ceil((b ** 2 - a ** 2) ** 0.5)
    print(3 * c + 1)
else:
    print(1)
