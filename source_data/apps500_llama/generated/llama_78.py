import sys

def input(): return sys.stdin.readline().rstrip("\r\n")
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from bisect import bisect_left
from sys import stdout

def main():
    n = int(input())
    h = read_int_list()
    res = h[:]
    for i in range(n - 1):
        if res[i] + 2 <= res[i + 1]:
            res[i] += 1
            res[i + 1] -= 1

    print(*res)

main()
