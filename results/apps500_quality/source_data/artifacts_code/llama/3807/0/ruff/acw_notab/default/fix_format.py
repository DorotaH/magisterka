import math

m = int(input())

cubes = [i**3 for i in range(1, 2 + int(math.sqrt(m)))]

cubes.sort(reverse=True)

max_blocks = 0
max_volume = 0
current_volume = 0
blocks = 0

for volume in cubes:
    if volume + current_volume > m:
        break
    current_volume += volume
    blocks += 1
    if current_volume == m:
        max_volume = m
        max_blocks = blocks
        break

if m > current_volume:
    current_volume += m - current_volume
    max_volume = m
    max_blocks += m - current_volume + 1

print(max_blocks, max_volume)
