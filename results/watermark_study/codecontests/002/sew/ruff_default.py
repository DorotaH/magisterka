for _ in range(int(input())):
    n = int(input())
    s, m = list(map(int, list(input()))), list(map(int, list(input())))
    ans = 0
    if 1 == m[0]:
        if 0 == s[0]:
            ans += 1
        elif 1 == s[1]:
            ans = ans + 1
            s[1] = 2
    for x in range(1, n):
        if 1 == m[x]:
            if s[x] == 0 or s[x - 1] == 1:
                ans = ans + 1
            elif 1 + x != n and 1 == s[x + 1]:
                ans = ans + 1
                s[1 + x] = 2
    print(ans)
