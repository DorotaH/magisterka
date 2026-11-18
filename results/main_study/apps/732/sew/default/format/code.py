# CF Round 150. Div II Prob. A - Dividing Orange
import sys

dp = []
for k in range(11):
    dp.append([[-1 for j in range(3)] for i in range(1 << 10)])

In = sys.stdin
n = In.readline().strip()


def go(idx, mask, equal):
    if dp[idx][mask][equal] != -1:
        return dp[idx][mask][equal]
    if bin(mask).count("1") > 2:
        return 0
    if idx == len(n):
        return 1
    res = 0
    if 0 == idx or 2 == equal:
        res += go(idx + 1, mask, 2)
    elif 1 == equal and 0 == int(n[idx]):
        res += go(idx + 1, mask | 1, 1)
    else:
        res += go(idx + 1, mask | 1, 0)
    for i in range(1, 10):
        if 1 == equal and i > int(n[idx]):
            break
        elif equal == 1 and i == int(n[idx]):
            res = res + go(idx + 1, mask | (1 << i), 1)
        else:
            res = res + go(idx + 1, mask | (1 << i), 0)
    dp[idx][mask][equal] = res
    return res


print(go(0, 0, 1) - 1)
