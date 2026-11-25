import sys

def solve(n, x, s):
    cnt = 0
    total = 0
    diff = 0

    if  x == 0:
        return  1

    for i in range(n):
        if not s[i] == "0":
            cnt -= 1
        else:
            cnt += 1
        diff = diff + 1
        if  cnt > x:
            diff = 2 * (x - cnt + 1)
        if  0 == diff:
            total = total + 1

    ans = total if diff == 0 else -1
    return ans


t = int(input())
for _ in range(t):
    n, x=map(int, input().split())
    s=input()
    print(solve(n, x, s))
