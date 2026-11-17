for _ in range(0, int(input())):
    n = int(input())
    s, m = list(map(int, list(input()))), list(map(int, list(input())))
    ans = 0
    if m[0] == 1:
        if s[0] == 0:
            ans += 1
        elif s[1] == 1:
            ans = ans + 1
            s[1] = 2
    for x in range(1, n):
        if m[x] == 1:
            if s[x] == 0 or s[x - 1] == 1:
                ans = ans + 1
            elif 1 + x != n and s[x + 1] == 1:
                ans = ans + 1
                s[1 + x] = 2
    print(ans)
