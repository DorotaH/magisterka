def find_pocket(n, m, x, y, v_x, v_y):
    if v_x == 0:
        if v_y == 0:
            return -1
        if v_y == 1:
            if y == m:
                return n, 0
            else:
                return -1
        if v_y == -1:
            if y == 0:
                return n, m
            else:
                return -1
    if v_y == 0:
        if v_x == 1:
            if x == n:
                return 0, m
            else:
                return -1
        if v_x == -1:
            if x == 0:
                return n, m
            else:
                return -1
    if v_x == v_y:
        if v_x == 1:
            if x == n or y == m:
                return n, 0
            else:
                return -1
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
