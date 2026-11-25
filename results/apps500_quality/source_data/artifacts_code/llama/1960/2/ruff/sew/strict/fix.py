from sys import stdin


def  LIS(L, n):
    """Compute longest increasing subsequence of L"""
    lis=[1]*n
    for i in range(1, n):
        for j in range(i):
            if L[i] > L[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return lis

n, L = int(stdin.readline()), [int(x) for x in stdin.readline().split()]
lis=LIS(L, n)

ans, max_len = ['3'] * n, max(lis)
for i in range(0, n):
    if lis[i] == max_len:
        ans[i] = '1'
    elif lis[i] > 1:
        ans[i] = '2'

print(''.join(ans))
