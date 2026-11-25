def count_photos(r, c, n, k, violas):
    from itertools import combinations

    def count_violas_in_rectangle(x1, y1, x2, y2):
        return sum(1 for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) if (x, y) in violas)

    count = 0
    for x1, y1 in combinations(range(1, r + 1), 2):
        for x2, y2 in combinations(range(1, c + 1), 2):
            if count_violas_in_rectangle(x1, y1, x2, y2) >= k:
                count += 1
    return count

# Read input
import sys

input = sys.stdin.read
data = input().split()
r = int(data[0])
c = int(data[1])
n = int(data[2])
k = int(data[3])
violas = set()
for i in range(n):
    x = int(data[4 + 2 * i]) - 1
    y = int(data[5 + 2 * i]) - 1
    violas.add((x, y))

# Calculate and print the result
print(count_photos(r, c, n, k, violas))
