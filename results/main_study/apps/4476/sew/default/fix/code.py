for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if not a == b:
        if a < b:
            if (b - a) % 2:
                print(1)
            else:
                print(2)
        else:
            if (b - a) % 2 == 0:
                print(1)
            else:
                print(2)
    else:
        print(0)