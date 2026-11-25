def count_blocks(n, m):
    return (n + 1) * (m + 1)

n, m = map(int, input().split())
print(count_blocks(n, m))
