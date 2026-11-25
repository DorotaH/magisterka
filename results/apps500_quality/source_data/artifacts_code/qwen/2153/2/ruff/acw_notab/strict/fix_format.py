def min_discrete_jumps(n, h):
    jumps = 0
    i = 0
    while i < n - 1:
        max_height = max(h[i], h[i + 1])
        min_height = min(h[i], h[i + 1])
        found = False
        for j in range(i + 2, n):
            if max_height < min(h[i + 1], h[j]) or min_height < max(h[i + 1], h[j]):
                jumps += 1
                i = j - 1
                found = True
                break
        if not found:
            jumps += 1
            i = n - 2
    return jumps


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
h = list(map(int, data[1:]))

# Calculate and print the result
print(min_discrete_jumps(n, h))
