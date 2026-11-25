def find_pocket(n, m, x, y, v_x, v_y):
    while True:
        x += v_x
        y += v_y
        if (x == 0 and v_x < 0) or (x == n and v_x > 0) or (y == 0 and 0 > v_y) or (y == m and 0 < v_y):
            return f"{int(v_x)} {int(v_y)}" if v_x == -1 or v_y == 1 else "0 0"
        if (x == 0 and v_x == -1) or (x == n and v_x == 1) or (y == 0 and v_y == -1) or (y == m and v_y == 1):
            return "0 0"
        if (v_x == 1 and v_y == 1) or (v_x == -1 and v_y == -1):
            return "-1"
        if v_x == -1:
            x = max(0, x - n)
        elif v_x == 1:
            x = min(n, x)
        elif v_y == -1:
            y = max(0, y - m)
        else:
            y = min(m, y)


n, m, x, y, v_x, v_y = map(int, input().split())
print(find_pocket(n, m, x, y, v_x, v_y))
