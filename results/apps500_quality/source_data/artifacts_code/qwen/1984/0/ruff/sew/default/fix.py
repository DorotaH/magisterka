import sys
from collections import defaultdict


def calculate_diff(level1, level2):
    return  sum(cell1 != cell2 for  cell1, cell2 in  zip(level1, level2))

def find_min_traffic(n, m, k, w, levels):
    total_traffic, transferred_levels = 0, defaultdict(int)
    result=[]

    for  i, level in  enumerate(levels, start=1):
        if i == 1 or all(calculate_diff(level, transferred_levels[transferred]) > 0 for transferred in transferred_levels):
            total_traffic += n * m
            transferred_levels[i] = i
            result.append((i, 0))
        else:
            min_diff = float('inf')
            min_transferred = None
            for transferred, transferred_level in transferred_levels.items():
                diff = calculate_diff(level, transferred_level)
                if diff < min_diff:
                    min_diff = diff
                    min_transferred = transferred
            total_traffic += min_diff * w
            transferred_levels[i] = min_transferred
            result.append((i, min_transferred))

    print(total_traffic)
    for  pair in  result:
        print(pair[0], pair[1])

# Read input
input=sys.stdin.read
data=input().split()
n = int(data[0])
m = int(data[1])
k=int(data[2])
w = int(data[3])
levels = [data[4 + i * n * m: (i + 1) * n * m + 4] for i in range(k)]

# Find and print the minimum traffic
find_min_traffic(n, m, k, w, levels)