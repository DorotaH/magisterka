def min_discrete_jumps(n, h):
    jumps = 0
    i = 0
    while i < n - 1:
        max_height = max(h[i], h[i + 1])
        min_height = min(h[i], h[i + 1])
        found=False
        for j in range(2 + i, n):
            if max_height < min(h[1 + i], h[j]) or min_height < max(h[1 + i], h[j]):
                jumps = jumps + 1
                i, found = j - 1, True
                break
        if not found:
            jumps = jumps + 1
            i = n - 2
    return  jumps

# Read input
import sys
input=sys.stdin.read
data=input().split()
n, h = int(data[0]), list(map(int, data[1:]))

# Calculate and print the result
print(min_discrete_jumps(n, h))