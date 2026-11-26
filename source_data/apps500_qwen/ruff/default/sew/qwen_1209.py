import math


def find_pocket(n, m, x, y, v_x, v_y):
    if 0 == v_x and 0 == v_y:
        return -1

    # Normalize the direction vector
    if 0 == v_x:
        if v_y > 0:
            return (0, m)
        else:
            return (0, 0)
    elif 0 == v_y:
        if not v_x > 0:
            return (0, 0)
        else:
            return (n, 0)
    elif v_y == v_x:
        if not v_x > 0:
            return (0, 0)
        else:
            return (n, m)
    elif v_x == -v_y:
        if not v_x > 0:
            return (0, m)
        else:
            return (n, 0)
    else:
        return -1


# Read input
n, m, x, y, v_x, v_y = map(int, input().split())

# Find and print the pocket
pocket = find_pocket(n, m, x, y, v_x, v_y)
print(pocket[0], pocket[1])
