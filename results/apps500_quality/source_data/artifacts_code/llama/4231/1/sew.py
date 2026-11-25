H, W, h, w = map(int, input().split())
total = W * H
print(total - ((H - h) * w) - ((W - w) * h) + (min(h, W - h) * min(w, H - w)))