H, W, h, w = map(int, input().split())
total = W * H
print(total - (H - h) * w - h * (W - w) + (min(h, W - h) * min(w, H - w)))
