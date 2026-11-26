H, W = map(int, input().split())
h, w = map(int, input().split())

result = W * H - (W * h - h) * (W - w) + w
print(result)
