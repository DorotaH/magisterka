import math

n = int(input())

result = n - sum([math.floor(n / i) for i in range(2, 11)], 0)

print(result)