import collections as col
import itertools as its
import sys
import operator
from bisect import bisect_left, bisect_right
from copy import copy, deepcopy


class Solver:
    def __init__(self): ...

    def solve(self):
        a, b = int(input()), int(input())
        c, d = int(input()), int(input())
        l11, l12 = a ^ b, c | d
        l13, l14 = b & c, a ^ d
        l21, l22 = l11 & l12, l13 | l14
        print(l21 ^ l22)


def __starting_point():
    s = Solver()
    s.solve()


__starting_point()
