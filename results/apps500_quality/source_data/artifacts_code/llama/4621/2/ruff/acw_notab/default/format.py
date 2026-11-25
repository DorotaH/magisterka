import math

H, W = map(int, input().split())
image = [list(input()) for _ in range(H)]

new_image = []
for i in range(H):
    new_image.append([])
    for j in range(W):
        new_image[i].append(image[math.floor((i + 1) / 2)].strip()[j])

for i in range(H):
    for j in range(W):
        print(new_image[i][j], end="")
    print()
