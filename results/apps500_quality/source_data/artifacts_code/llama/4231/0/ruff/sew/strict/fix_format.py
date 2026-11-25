H, W = map(int, input().split())
h, w = map(int, input().split())

result = (H * W) - ((h * W - h) * (W - w)) + w
print(result)
