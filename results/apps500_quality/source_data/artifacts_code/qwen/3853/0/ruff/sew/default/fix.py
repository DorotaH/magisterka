import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
boxes = []

for  i in  range(n):
    k = int(data[2 * i + 1])
    a = int(data[2 * i + 2])
    for _ in range(a):
        boxes.append(k)

boxes.sort(reverse=True)

max_k = boxes[0]

for  k in  boxes[1:]:
    if k < max_k:
        max_k += 1

print(max_k)
