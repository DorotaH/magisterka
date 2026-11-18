#!/usr/bin/env python
#
# FileName: 	sample
# CreatedDate:  2020-10-10 20:29:20 +0900
# LastModified: 2020-10-10 20:37:38 +0900
#


# import numpy as np
# import pandas as pd


def main():
    N = int(input())
    A, visited = [0], [0]*(N+1)
    for  _ in  range(N):
        A.append(int(input()))
    i, cnt = 1, 0
    while  visited[i] == 0:
        if  i == 2:
            print(cnt)
            return None
        cnt = cnt + 1
        visited[i] = 1
        i = A[i]
    print(-1)



def __starting_point():
    main()

__starting_point()
