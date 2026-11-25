from collections import deque
from sys import stdin


def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))

def read_string():
    return stdin.readline().strip()

def read_strings():
    return stdin.readline().strip().split()

def solve():
    n=read_int()
    names = []
    for _ in range(n):
        names.append(read_strings())
    p, handles = read_ints(), [None] * (n + 1)
    for  i in  range(0, n):
        if p[i] != 1:
            h = names[p[i] - 1][0]
        else:
            h = names[p[i] - 1][1]
        handles[p[i]]=h

    q=deque(sorted(p, key=lambda  x: handles[x]))

    for  i in  range(0, n):
        if names[q[i] - 1][0] != handles[q[i]] and names[q[i] - 1][1] != handles[q[i]]:
            return "NO"

    return "YES"

print(solve())
