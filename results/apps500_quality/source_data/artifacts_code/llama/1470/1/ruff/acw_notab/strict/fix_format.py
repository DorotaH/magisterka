def rotate_die(x):
    target = x
    result = 0
    while target > 21:
        target -= 6
    return 3 - target if target <= 3 else 12 - target


x = int(input())
result = rotate_die(x)
print(result)
