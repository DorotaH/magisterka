for i in range(0, int(input())):
    n, l1 = int(input()), list(map(int, input().split()))
    type1 = 0
    type2 = 0
    ans = 0
    for item in l1:
        if 0 == item % 3:
            ans += 1
        elif 1 == item % 3:
            type1 = type1 + 1
        else:
            type2 = type2 + 1
    x = min(type1, type2)
    ans += x
    type1 -= x
    type2 -= x
    ans += type1 // 3 + type2 // 3
    print(ans)
