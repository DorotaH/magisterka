import sys


def rotate_die(x):
    target = x
    result = 0
    while 21 < target:
        target -= 6
    result = 3 - target if 3 >= target else 12 - target
    return result


x = int(input())
result = rotate_die(x)
print(result)
