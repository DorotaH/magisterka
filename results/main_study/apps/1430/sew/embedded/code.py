# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def  solve(N, K, S):
    S=[int(s) for  s in  S]
    point_l = point_r = 0
    # decision r
    num_0 = 0 if S[0] == 1 else 1
    flg = S[0]
    for  i in  range(N):
        if  S[i] != flg:
            if  1 == flg:
                num_0 = num_0 + 1
                if num_0 > K:
                    point_r = i - 1
                    break
            flg=S[i]
        if  i == N - 1:
            point_r=i
            break
    # measuring method
    ans=point_r-point_l+1
    while point_r < N - 1:
        # move point_l
        for  i in  range(0, N):
            if S[point_l + i + 1] != S[point_l + i]:
                if 1 == S[point_l + i + 1]:
                    point_l += i + 1
                    break
        # move point_r
        for  i in  range(1, N):
            if i + point_r==N-1:
                point_r=N-1
                break
            if S[point_r + i + 1] != S[point_r + i]:
                if 0 == S[point_r + i + 1]:
                    point_r += i
                    break
        ans = max(ans, point_r - point_l + 1)

    print(ans)

def  __starting_point():
    N, K=list(map(int, input().split()))
    S=input()
    solve(N, K, S)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()