import math

def max_blocks(m):
    def count_blocks(x):
        return sum((x // (i * i) for i in range(1, int(math.sqrt(x)) + 1)))

    max_vol = 0
    max_blocks_num = 0
    for x in range(1, m + 1):
        vol = x
        blocks = 1
        for i in range(1, int(math.sqrt(x)) + 1):
            blocks += (x // (i * i))
            vol -= (x // (i * i)) * (i * i)
        if blocks > max_blocks_num or (blocks == max_blocks_num and vol > max_vol):
            max_blocks_num = blocks
            max_vol = vol
    return max_blocks_num, max_vol

m = int(input())
print(*max_blocks(m))
