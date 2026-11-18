import sys

input = sys.stdin.readline
n, M = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = []
tmp = [0] * 101
for i in range(0, n):
    num, T = 0, t[i]
    for  j in  range(1, 101):
        if not T + j * tmp[j] <= M:
            m = M - T
            num += m // j
            break
        else:
            num += tmp[j]
            T += j * tmp[j]

    ans.append(i-num)
    tmp[t[i]]+=1

print(*ans)
