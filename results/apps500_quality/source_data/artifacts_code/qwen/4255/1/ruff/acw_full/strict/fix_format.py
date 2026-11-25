import sys

input = sys.stdin.read
data = input().split()
AB = int(data[0])
BC = int(data[1])
CA = int(data[2])

# Since it's a right triangle, the area can be calculated as (1/2) * base * height
# Here, we can consider AB and BC as the base and height respectively
area = (1 / 2) * AB * BC
print(int(area))
