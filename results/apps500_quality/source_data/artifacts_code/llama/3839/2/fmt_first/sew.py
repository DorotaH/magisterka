def  solve():
    n = int(input())

    x, y = (n - 1) // 4 * 4 + 2, 1

    for i in range(x, x+(n - 1) % 4+1):
        if i == x:
            print(i, y)
        else:
            print(i, y + (i - x) // 2)

        if i % 4 == 3:
            y = y + 2

    for i in range(x-1, x-4 * ((n - 1) % 4)-1, -1):
        if i == x - 1:
            print(i, y)
        else:
            print(i, y - (x - i) // 2)

        if i % 4 == 1:
            y = y + 2


solve()