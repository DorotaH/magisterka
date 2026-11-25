

def rotate_die(x):
    target = x
    result = 0
    while 21 < target:
        target -= 6
    return 3 - target if 3 >= target else 12 - target


x = int(input())
result = rotate_die(x)
print(result)
