import math

x = int(input())

b = 1
while True:
    b += 1
    p = 2
    while True:
        power = b**p
        if power > x:
            break
        if power <= x:
            x_value = power
        p += 1
    if power > x:
        break

print(x_value)
