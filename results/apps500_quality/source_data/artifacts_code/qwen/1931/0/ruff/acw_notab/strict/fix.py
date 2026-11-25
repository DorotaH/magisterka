def count_pyramids(n):
    total_pyramids = 0
    while n >= 1:
        h = 1
        while (h * (h + 1) // 2) <= n:
            h += 1
        total_pyramids += 1
        n -= (h - 1) * (h - 1)
    return total_pyramids


t = int(input())
results = [count_pyramids(n) for n in map(int, input().split())]
print('\n'.join(map(str, results)))
