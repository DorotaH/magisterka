import math

def solve():
    R, x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    if d > R:
        print(x1 + dx / d * R, y1 + dy / d * R, R, sep=' ')
    else:
        r = R - d
        print(x1 + dx / d * r, y1 + dy / d * r, r, sep=' ')

solve()
