
n, m, x, y, vx, vy = map(int, input().split())

dx = 2 * abs(vx)
dy = 2 * abs(vy)

if dx == 0:
    x_direction = 0
    if vy > 0:
        y_direction = 1
    else:
        y_direction = -1

    if y + y_direction * dy <= 0:
        print(-1)
    else:
        print(0, -1)
elif dy == 0:
    y_direction = 0
    if vx > 0:
        x_direction = 1
    else:
        x_direction = -1

    if x + x_direction * dx <= 0:
        print(-1)
    else:
        print(1, 0)
else:
    if vx > 0:
        x_direction = 1
    else:
        x_direction = -1

    if vy > 0:
        y_direction = 1
    else:
        y_direction = -1

    x += x_direction * dx
    y += y_direction * dy

    if x > n or y > m or x <= 0 or y <= 0:
        if x > n or y > m:
            print(x - n, y - m)
        else:
            print(-1)
    else:
        print(-1)
