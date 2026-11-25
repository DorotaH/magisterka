import sys
import math
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from collections import deque
from itertools import permutations, combinations
import bisect
import sys


def solve():
	n, m, k = map(int, input().split())
	alarm_clocks = list(map(int, input().split()))

	alarm_clocks.sort()
	alarm_clocks = alarm_clocks + [0]

	ans = 0
	for i in range(1, len(alarm_clocks)):
		alarm_clocks[i] += alarm_clocks[i - 1]

	alarm_clocks = dict(enumerate(alarm_clocks))

	curr = 0
	curr_alarm = 0
	for i in range(1, 10**6 + 1):
		if i in alarm_clocks:
			curr += 1
			curr_alarm = max(curr_alarm, alarm_clocks[i])
		else:
			if k <= curr:
				if curr_alarm - i + 1 >= m:
					ans += 1
					curr = 0
			else:
				curr = 0
			curr_alarm = 0
	print(n - ans)


solve()
