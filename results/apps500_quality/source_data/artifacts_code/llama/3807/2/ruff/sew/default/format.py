import math

m = int(input())


def max_blocks(m):
    n = 0
    blocks = 0
    total_volume = 0
    i = 1
    while i <= m:
        blocks_in_i = int(pow((i**3 + 2 * i**2 - 1), 0.5) - pow(i, 2) - 1) // 2
        if blocks_in_i > 0:
            total_volume, blocks = i**3 + blocks_in_i * i**2, blocks_in_i + 1
            n = i
        i = i + 1
    return blocks, n * n


blocks, volume = max_blocks(m)
print(blocks, volume)
