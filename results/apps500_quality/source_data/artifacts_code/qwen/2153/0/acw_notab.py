import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
heights = list(map(int, data[1:]))


def min_discrete_jumps(heights):
    jumps = 0
    i = 0
    while i < n - 1:
        max_height = max(heights[i], heights[i + 1])
        min_height = min(heights[i], heights[i + 1])
        found = False
        for j in range(i + 2, n):
            if (max_height < heights[j] < min_height) or (min_height < heights[j] < max_height):
                jumps += 1
                i = j
                found = True
                break
        if not found:
            i += 1
    return jumps


print(min_discrete_jumps(heights))
