H, W = map(int, input().split())
image = [list(input().strip()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        print(image[H - i - 1][j], end='')
    print()

for i in range(H):
    for j in range(W):
        print(image[H - i - 1][j], end='')
    print()
