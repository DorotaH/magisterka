def  count_blocks(n, m):
    return  (1 + n) * (1 + m)

n, m = map(int, input().split())
print(count_blocks(n, m))