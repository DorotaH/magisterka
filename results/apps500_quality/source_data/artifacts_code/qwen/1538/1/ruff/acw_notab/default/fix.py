def min_visible_boxes(n, a):
    a.sort()
    visible_boxes = n
    for i in range(1, n):
        if a[i - 1] < a[i]:
            visible_boxes -= 1
    return visible_boxes


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
a = list(map(int, data[1:]))

# Calculate and print the result
print(min_visible_boxes(n, a))
