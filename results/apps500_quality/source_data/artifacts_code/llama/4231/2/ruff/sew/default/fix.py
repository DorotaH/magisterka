H, W, h, w = map(int, input().split())
print((H * W) - (h * (W - w)) - (w * (H - h)) + ((min(H, w) - 1) * (min(H, w) - 1)))