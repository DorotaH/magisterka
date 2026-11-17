import os.path
import sys
from collections import *

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")

input = sys.stdin.readline

##########################################################


def solve():
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    x = sum(arr)
    if k >= sum(arr):
        print(0)
        return
    arr.sort()
    pos = 0
    Sum = 0

    res = 1e16
    while pos < n:
        Sum += arr[pos]
        x = Sum - arr[0]
        # print(x)
        x = k - x
        y = n - pos
        z = min(x // y, arr[0])
        # print(Sum,x,y,z)
        res = min(res, arr[0] - z + y - 1)
        pos += 1
    print(res)


t = int(input())
while t:
    t -= 1
    solve()


##########################################################
