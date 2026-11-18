for _ in range(0, int(input())):
    n, ar = int(input()), list(map(int, input().split()))
    a, b=0, 0
    for  elem in  ar:
        if not elem % 2 == 0:
            b = 1
        else:
            a = 1
    if  1 == sum(ar) % 2:
        print('YES')
    elif  a == 1 == b:
        print('YES')
    else:
        print('NO')