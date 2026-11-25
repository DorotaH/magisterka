import math

k, n, s, p = map(int, input().split())

total_airplanes = n * k
total_sheets = total_airplanes * s

required_packs = math.ceil(total_sheets / p)

print(required_packs)