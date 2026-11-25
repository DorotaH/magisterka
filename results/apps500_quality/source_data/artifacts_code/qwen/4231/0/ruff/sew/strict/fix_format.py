import sys

input = sys.stdin.read
data = input().split()

H, W = int(data[0]), int(data[1])
h, w = int(data[2]), int(data[3])

remaining_cells = ((H - h) * W) + ((W - w) * h)
print(remaining_cells)
