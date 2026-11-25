def count_pictures(r, c, n, k, violas):
    count = 0
    for i in range(r):
        for j in range(c):
            viola_count = 0
            for x in range(i, r):
                for y in range(j, c):
                    if (x + 1, y + 1) in violas:
                        viola_count += 1
                    if viola_count >= k:
                        count += 1
                        break
                if viola_count >= k:
                    break
    return count


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
r = int(data[0])
c = int(data[1])
n = int(data[2])
k = int(data[3])
violas = set()
for _ in range(n):
    x = int(data[4 + 2 * _])
    y = int(data[5 + 2 * _])
    violas.add((x, y))

# Count and print the number of pictures
result = count_pictures(r, c, n, k, violas)
print(result)
