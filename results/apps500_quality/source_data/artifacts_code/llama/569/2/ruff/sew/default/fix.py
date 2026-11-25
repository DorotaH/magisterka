from collections import defaultdict
from sys import stdin


def  read_int():
    return  int(stdin.readline())


def  read_ints():
    return  map(int, stdin.readline().split())


def  read_str():
    return  stdin.readline().strip()


def  read_strs():
    return  stdin.readline().split()


def  solve():
    n, s = read_int(), read_str()

    d=defaultdict(int)
    for i in range(n):
        for  j in  range(1 + i, 1 + n):
            d[tuple(s[i:j])]+=1
            if  d[tuple(s[i:j])] > 1:
                return  -1

    ans=0
    for i in range(n):
        for  j in  range(1 + i, n):
            if  s[i] == s[j]:
                ans += 1
                s=s[0:i]+chr(1 + ord(s[i]))+s[1 + i:j]+s[1 + j:]
    return  ans

print(solve())