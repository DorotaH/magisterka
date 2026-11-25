import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
h = list(map(int, data[1:]))

# Initialize a list to keep track of the number of slides for each mountain
slides = [0] * n

# Iterate over the mountains and count the number of slides
for i in range(n - 1):
    while h[i] + 2 <= h[i + 1]:
        slides[i] += 1
        slides[i + 1] -= 1
        h[i] += 1
        h[i + 1] -= 1

# Output the final heights of the mountains
print(" ".join(map(str, h)))
