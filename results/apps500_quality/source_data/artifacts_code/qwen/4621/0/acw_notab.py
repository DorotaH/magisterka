import sys
input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])

image = [data[i + 2] for i in range(H)]
extended_image = []
for row in image:
    extended_image.extend(row for _ in range(2))
for row in extended_image:
    print(row)
