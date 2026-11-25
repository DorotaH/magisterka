import sys
input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])

image = []
for i in range(H):
    image.append(data[2 + i])

extended_image = list()
for  row in  image:
    for _ in range(2):
        extended_image.append(row)

for  row in  extended_image:
    print(row)
