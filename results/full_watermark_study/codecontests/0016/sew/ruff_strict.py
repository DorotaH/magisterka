from sys import stdin

tt = 1

for loop in range(tt):
    n, k = map(int, stdin.readline().split())
    c = list(map(int, stdin.readline().split()))
    for i in range(n * k):
        c[i] -= 1

    last = [None] * n

    RLC = []
    for i in range(n * k):
        if not last[c[i]] == None:
            RLC.append((i, last[c[i]], c[i]))
            last[c[i]] = i
        else:
            last[c[i]] = i

    RLC.sort()

    end, rem = [False] * n, [(n + k - 2) // (k - 1)] * (n * k)

    ans = [None] * n

    for R, L, C in RLC:
        if end[C] or min(rem[L : R + 1]) == 0:
            continue
        else:
            end[C] = True
            ans[C] = (L, R)
            for i in range(L, 1 + R):
                rem[i] -= 1

    for i in ans:
        print(i[0] + 1, i[1] + 1)
