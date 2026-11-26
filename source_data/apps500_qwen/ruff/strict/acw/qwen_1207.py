def find_pocket(n, m, x, y, v_x, v_y):
    if v_x == 0:
        if v_y == 0:
            return -1
        if v_y == -1:
            return (n, m) if y == 0 else -1
        elif v_y == 1:
            return (n, 0) if y == m else -1
    if v_y == 0:
        if v_x == -1:
            return (n, m) if x == 0 else -1
        elif v_x == 1:
            return (0, m) if x == n else -1
    if v_x == v_y:
        if v_x == 1:
            return (n, 0) if x == n or y == m else -1
        if v_x == -1:
            if x == 0 or y == 0:
                return n, m
            else:
                return -1
    if v_x == -v_y:
        if v_x == 1:
            if x == n or y == 0:
                return 0, m
            else:
                return -1
        if v_x == -1:
            if x == 0 or y == m:
                return n, 0
            else:
                return -1
    return -1


# Read input
n, m, x, y, v_x, v_y = map(int, input().split())

# Find the pocket
result = find_pocket(n, m, x, y, v_x, v_y)

# Print the result
if result == -1:
    print(-1)
else:
    print(result[0], result[1])
