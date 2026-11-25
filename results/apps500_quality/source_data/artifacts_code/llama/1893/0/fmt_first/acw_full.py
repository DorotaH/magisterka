import math

n, t = map(int, input().split())
initial_value = n
growth_rate = 1.000000011

result = (growth_rate**t) * initial_value

print(f"{result:.12f}")
