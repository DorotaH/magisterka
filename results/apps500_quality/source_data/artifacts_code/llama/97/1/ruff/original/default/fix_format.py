n, m, x, y, vx, vy = map(int, input().split())

dx, dy = vx, vy
if vx == 0:
    dx = 1 if vy > 0 else -1
elif vy == 0:
    dy = 1 if vx > 0 else -1
elif vx == dy:
    dx, dy = 1, 1
else:
    dx, dy = -1, -1

if dx < 0:
    x -= 1
if dy < 0:
    y -= 1

steps = 0
while 0 <= x < n and 0 <= y < m:
    x += dx
    y += dy
    steps += 1

if 0 <= x < n and 0 <= y < m:
    print(x % n, y % m)
else:
    print(-1)
