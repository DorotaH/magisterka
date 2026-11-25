import  math

x = int(input())

b = 1
while 1:
    b = b + 1
    p=2
    while 1:
        power=b**p
        if  x < power:
            break
        if  power <= x:
            x_value=power
        p = p + 1
    if x < power:
        break

print(x_value)