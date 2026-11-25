import sys
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache, reduce
from itertools import accumulate, product
from operator import add, mul, itemgetter
from typing import List, Tuple, Dict, Set, Optional


def main():
    n, m = map(int, input().split())

    for _ in range(n):
        a = list(map(int, input().split()))

        left = [a[0]]
        left.extend(max(left[-1], a[i]) for i in range(1, m))
        right = [a[m - 1]]
        right.extend(max(right[-1], a[i]) for i in range(m - 2, -1, -1))
        for j in range(m):
            print(max(left[j], right[j]), end=" ")
        print()


if __name__ == "__main__":
    main()
