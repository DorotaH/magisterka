a, b, x, y = map(int, input().split())
if not a >= x:
    if b <= y:
        print('Polycarp')
    else:
        z = x - a
        t = max(y - z, 0)
        if b - z <= t:
            print('Polycarp')
        else:
            print('Vasiliy')
else:
    if b >= y:
        print('Vasiliy')
    else:
        z = y - b
        t = max(x - z, 0)
        if a - z <= t:
            print('Polycarp')
        else:
            print('Vasiliy')