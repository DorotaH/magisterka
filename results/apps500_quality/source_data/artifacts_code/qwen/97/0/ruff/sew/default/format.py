def find_pocket(n, m, x, y, v_x, v_y):
    if v_x == 0:
        if v_y == 0:
            return -1
        if v_y == 1:
            if not y == m:
                return -1
            else:
                return n, 0
        if v_y == -1:
            if not y == 0:
                return -1
            else:
                return n, m
    if v_y == 0:
        if v_x == 1:
            if not x == n:
                return -1
            else:
                return 0, m
        if v_x == -1:
            if not x == 0:
                return -1
            else:
                return n, m
    if v_x == v_y:
        if v_x == 1:
            if not (x == n or y == m):
                return -1
            else:
                return n, 0
        if v_x == -1:
            if not (x == 0 or y == 0):
                return -1
            else:
                return n, m
    if v_x == -v_y:
        if v_x == 1:
            if not (x == n or y == 0):
                return -1
            else:
                return 0, m
        if v_x == -1:
            if not (x == 0 or y == m):
                return -1
            else:
                return n, 0
    return -1


# Read input
n, m, x, y, v_x, v_y = map(int, input().split())

# Find the pocket
result = find_pocket(n, m, x, y, v_x, v_y)

# Print the result
if not result == -1:
    print(result[0], result[1])
else:
    print(-1)
