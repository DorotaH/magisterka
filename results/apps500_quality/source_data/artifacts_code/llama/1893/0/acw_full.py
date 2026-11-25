import math

n, t = map(int, input().split())
initial_value = n
growth_rate = 1.000000011

result = initial_value * (growth_rate ** t)

print(f"{result:.12f}")
