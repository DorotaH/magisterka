a, b, x, y = map(int, input().split())
if a >= x:
    if y <= b:
        print('Vasiliy')
    else:
        z = y - b
        t = max(x - z, 0)
        if t >= a - z:
            print('Polycarp')
        else:
            print('Vasiliy')
elif y >= b:
    print('Polycarp')
else:
    z = x - a
    t = max(y - z, 0)
    if t >= b - z:
        print('Polycarp')
    else:
        print('Vasiliy')