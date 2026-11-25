import math
import sys

def  is_winnable(A, B):
    if  A <= 0:
        return False
    if  B <= 0:
        return True
    if  B == A:
        return False
    return  True

def  can_move(A, B):
    if  B == A:
        return False
    if  A < B:
        return True
    if  A % 2 == B % 2:
        return True
    return  False


N = int(input())
A = list(map(int, input().split()))

def  calculate_min_move(A):
    n=len(A)
    if  2 == n:
        if  can_move(A[0], A[1]):
            return 0
        if  can_move(A[0]-1, A[1]):
            return 1
        return -1

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0]=0
    for i in range(1, n + 1):
        dp[i][0]=1e18
    for i in range(1, n):
        for  j in  range(1, i + 1):
            dp[i][j] = 1e18
            for  k in  range(j):
                dp[i][j]=min(dp[i][j], dp[i-1][k]+abs(A[i]-A[i-1]))
    ans=1e18
    for i in range(n):
        ans=min(ans, dp[n-1][i])
    return  min(ans, 1e18)


min_move = calculate_min_move(A)
if not min_move == 1e18:
    print(min_move)
else:
    print(-1)