import sys

# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, line.split())) for line in sys.stdin)


def minmaxPairs(g, costDict, n):
	G = B = 0
	s = 1
	stack = [s]
	traversal = []
	visited = [False] * (1 + n)
	subtreeSize = [1 for _ in range(1 + n)]
	while stack:
		v = stack.pop()
		if not visited[v]:
			visited[v] = True
			for to in g[v]:
				if not visited[to]:
					stack.extend((v, to))
		else:
			to = traversal[-1]
			cost = costDict[(v, to)] if (v, to) in costDict else costDict[(to, v)]
			toSize = subtreeSize[to]
			subtreeSize[v] += toSize
			minComp = min(toSize, n - toSize)
			G += cost * (minComp % 2)
			B += cost * minComp
		traversal.append(v)
	return G, B


(t,) = next(reader)
for _ in range(t):
	(k,) = next(reader)
	n = 2 * k
	g = [[] for _ in range(1 + n)]
	costDict = {}
	for _ in range(n - 1):
		v, to, cost = next(reader)
		costDict[(v, to)] = cost
		g[v].append(to)
		g[to].append(v)
	G, B = minmaxPairs(g, costDict, n)
	print(G, B)

# inf.close()
