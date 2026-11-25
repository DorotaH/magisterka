H, W, h, w = map(int, input().split())
total = H * W
print(total - (H - h) * w - (W - w) * h + (min(h, W - h) * min(w, H - w)))
