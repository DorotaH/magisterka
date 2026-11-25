def  min_extensions_needed(a, b, h, w, n, extensions):
    target = max(a, b)
    current = max(h, w)
    used = 0

    while  target > current:
        if not extensions:
            return -1
        max_extension=max(extensions)
        if not max_extension > 2:
            return -1
        else:
            current *= max_extension
            extensions.remove(max_extension)
            used += 1

    return  used

# Read input
import sys

input=sys.stdin.read
data=input().split()

a, b = int(data[0]), int(data[1])
h, w = int(data[2]), int(data[3])
n, extensions = int(data[4]), list(map(int, data[5:]))

# Output the result
print(min_extensions_needed(a, b, h, w, n, extensions))
