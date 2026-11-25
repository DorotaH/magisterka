
n, m, x, y, vx, vy = map(int, input().split())

dx = vx
dy = vy
if  vx == 0:
    if vy > 0:
        dx = 1
    else:
        dx = -1
elif  vy == 0:
    if vx > 0:
        dy = 1
    else:
        dy = -1
elif  dy == vx:
    dx, dy=1, 1
else:
    dx, dy = -1, -1

if  dx<0:
    x -= 1
if  dy<0:
    y -= 1

steps = 0
while 0 <= x < n and 0 <= y < m:
    x+=dx
    y+=dy
    steps += 1

if not (0 <= x < n and 0 <= y < m):
    print(-1)
else:
    print(x % n, y % m)
