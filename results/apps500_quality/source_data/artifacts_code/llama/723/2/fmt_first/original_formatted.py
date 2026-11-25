import sys


def min_photo_area():
    n = int(sys.stdin.readline())
    w = []
    h = []
    for _ in range(n):
        w_i, h_i = map(int, sys.stdin.readline().split())
        w.append(w_i)
        h.append(h_i)

    min_w = min(max(w), max(h))
    min_h = sum(min(w[i] for i in range(n))) + min_w

    area = min_w * min_h

    return area


print(min_photo_area())
