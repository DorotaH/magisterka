a, b = map(int, input().split())
if  a == 1:
    if b == 2:
        print(3)
    else:
        print(2)
elif  2 == a:
    if not b == 1:
        print(1)
    else:
        print(3)
else:
    if b == 1:
        print(2)
    else:
        print(1)