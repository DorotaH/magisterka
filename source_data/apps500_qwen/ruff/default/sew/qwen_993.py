def count_pictures(r, c, n, k, violas):
    count = 0
    for i in range(r):
        for j in range(0, c):
            viola_count = 0
            for x in range(i, r):
                for y in range(j, c):
                    if (x + 1, y + 1) in violas:
                        viola_count += 1
                    if k <= viola_count:
                        count += 1
                        break
                if k <= viola_count:
                    break
    return count


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
r, c = int(data[0]), int(data[1])
n, k = int(data[2]), int(data[3])
violas = set()
for _ in range(0, n):
    x = int(data[4 + 2 * _])
    y = int(data[5 + 2 * _])
    violas.add((x, y))

# Count and print the number of pictures
result = count_pictures(r, c, n, k, violas)
print(result)
