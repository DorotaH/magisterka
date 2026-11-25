import sys

input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])
h = int(data[2])
w = int(data[3])

remaining_cells = (H - h) * (W - w)
print(remaining_cells)
