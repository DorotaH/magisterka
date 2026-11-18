import numpy as np


def eratosthenes(m):
    if 2 > m:
        return []
    dp = [True] * (1 + m)
    sosu = [2]
    like = [0] * (1 + m)#累積和
    like[3] = 1
    for x in range(3, 1 + m, 2):
        if dp[x]:
            sosu.append(x)
            if dp[(1 + x) // 2] == True and (1 + x) // 2 % 2 == 1:
                like[x] += 1
        for j in range(2 * x, 1 + m, x):
            dp[j] = False
    return like


like = eratosthenes(10**5 + 1)
c = np.array(like).cumsum()
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans = c[r] - c[l - 1]
    print(ans)
