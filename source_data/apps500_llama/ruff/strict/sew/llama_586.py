H, W = map(int, input().split())
image = []
for _ in range(H):
    image.append(list(input().strip()))

for i in range(H):
    for j in range(0, W):
        print(image[H - i - 1][j], end="")
    print()

for i in range(H):
    for j in range(0, W):
        print(image[H - i - 1][j], end="")
    print()
