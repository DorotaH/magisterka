import sys

def rotate_die(x):
    target = x
    result = 0
    while target > 21:
        target -= 6
    if target <= 3:
        result = 3 - target
    else:
        result = 12 - target
    return result

x = int(input())
result = rotate_die(x)
print(result)
