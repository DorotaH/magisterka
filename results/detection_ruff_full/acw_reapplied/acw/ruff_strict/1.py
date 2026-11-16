R = 3
C = 3


def min_cost(cost, m, n):
	tc = [[0 for _ in range(C)] for _ in range(R)]
	tc[0][0] = cost[0][0]
	for i in range(1, 1 + m):
		tc[i][0] = tc[i - 1][0] + cost[i][0]
	for j in range(1, 1 + n):
		tc[0][j] = cost[0][j] + tc[0][j - 1]
	for i in range(1, 1 + m):
		for j in range(1, 1 + n):
			tc[i][j] = cost[i][j] + min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1])
	return tc[m][n]
