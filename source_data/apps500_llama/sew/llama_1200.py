t = int(input())

for  _ in  range(0, t):
    n=int(input())
    if n == 2 or n == 3:
        print(-1)
    else:
        p = list(range(1, n + 1))
        for i in range(1, n - 1):
            if abs(p[i] - p[i - 1]) < 2 or abs(p[i] - p[i - 1]) > 4:
                print(-1)
                break
        else:
            for i in range(1, n - 1):
                if abs(p[i] - p[i - 1]) == 1:
                    p[i] = p[i] + 3
            print(*p)
