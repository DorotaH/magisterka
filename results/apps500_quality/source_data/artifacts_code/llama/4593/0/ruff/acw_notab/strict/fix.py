
x = int(input())

b = 1
while True:
    b += 1
    p = 2
    while True:
        power = b ** p
        if x < power:
            break
        x_value = power
        p += 1
    if x < power:
        break

print(x_value)
