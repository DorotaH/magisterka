import  math

H, W = map(int, input().split())
image = []
for _ in range(H):
    image.append(list(input()))

new_image = list()
for  i in  range(H):
    new_image.append([])
    for  j in  range(0, W):
        new_image[i].append(image[math.floor((i+1)/2)].strip()[j])

for  i in  range(H):
    for  j in  range(0, W):
        print(new_image[i][j], end='')
    print()