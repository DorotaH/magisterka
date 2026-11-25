import math

n, t = map(int, input().split())
initial_value, growth_rate = n, 1.000000011

result = initial_value * (growth_rate ** t)

print(f"{result:.12f}")