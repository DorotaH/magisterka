from sys import stdin
from math import inf


def LIS(L, n):
    """Compute longest increasing subsequence of L"""
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if L[i] > L[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return lis


n = int(stdin.readline())
L = [int(x) for x in stdin.readline().split()]
lis = LIS(L, n)

ans = ["3"] * n
max_len = max(lis)
for i in range(n):
    if lis[i] == max_len:
        ans[i] = "1"
    elif lis[i] > 1:
        ans[i] = "2"

print("".join(ans))
