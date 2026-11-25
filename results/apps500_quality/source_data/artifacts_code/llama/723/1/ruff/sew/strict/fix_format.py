n = int(input())
s = 0
h = 0
for _ in range(n):
    w, h1 = map(int, input().split())
    s += w * h1
    h = max(h, h1)
    h1, w = w, h1
    s += w * h1
print((h * s) - min(h * w, s))
