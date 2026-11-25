def max_blocks(m):
    max_blocks = 0
    max_x = 0
    for  x in  range(1, m + 1):
        volume = blocks = 0
        a = 1
        while  volume + pow(a, 3) <= x:
            volume += a**3
            blocks += 1
            a += 1
        if  max_blocks < blocks:
            max_blocks, max_x = blocks, x
    return max_blocks, max_x

m = int(input())
print(max_blocks(m))
