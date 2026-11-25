import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

a.sort()

visible_boxes = 0
current_max = 0

for size in a:
    if size > current_max:
        visible_boxes += 1
        current_max = size

print(visible_boxes)
