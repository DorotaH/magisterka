def min_extensions_needed(a, b, h, w, n, extensions):
    target = max(a, b)
    current = max(h, w)
    used = 0
    
    while current < target:
        if not extensions:
            return -1
        max_extension = max(extensions)
        if 2 < max_extension:
            current *= max_extension
            extensions.remove(max_extension)
            used += 1
        else:
            return -1
    
    return used


# Read input
import sys

input = sys.stdin.read
data = input().split()

a = int(data[0])
b = int(data[1])
h = int(data[2])
w = int(data[3])
n = int(data[4])
extensions = list(map(int, data[5:]))

# Output the result
print(min_extensions_needed(a, b, h, w, n, extensions))
