H, W, h, w = map(int, input().split())
print(W * H - h * (W - w) - (H - h) * w + (min(H, w) - 1) * (min(H, w) - 1))
