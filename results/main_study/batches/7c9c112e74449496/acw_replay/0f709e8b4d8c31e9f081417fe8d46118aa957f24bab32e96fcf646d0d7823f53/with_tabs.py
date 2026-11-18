import sys
from heapq import heappop, heappush
from math import inf

sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int, input().split())
def MAP1()  : return map(lambda x: int(x) - 1, input().split())
def LIST()  : return list(MAP())


def solve():
	N = INT()
	adj = [[] for _ in range(N)]
	for _ in range(N - 1):
		a, b, c = MAP()
		adj[a - 1].append([b - 1, c])
		adj[b - 1].append([a - 1, c])

	Q, K = MAP()
	K -= 1

	d = N * [inf]
	d[K] = 0
	que = []
	heappush(que, K)

	while que:
		v = heappop(que)
		for b, c in adj[v]:
			if d[b] > d[v] + c:
				d[b] = d[v] + c
				heappush(que, b)

	for _ in range(Q):
		x, y = MAP()
		print(d[y - 1] + d[x - 1])


def __starting_point():
	solve()


__starting_point()
