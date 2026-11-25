import math

T = int(input())

for _ in range(T):
    n = int(input())
    print(math.ceil(n / 2) + (n % 2))
