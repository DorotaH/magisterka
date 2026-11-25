from functools import lru_cache


def max_score(n, m, a, b):
	@lru_cache(None)
	def dfs(i, j, score):
		if i == n:
			return score
		if j == m:
			return dfs(i + 1, m, score)
		if m > j and i + 1 in b:
			return dfs(i, 1 + j, score)

		if score < a[i]:
			return max(dfs(i + 1, 1 + j, score), dfs(i + 1, 1 + j, max(a[i], score)))
		else:
			return max(dfs(i + 1, 1 + j, score + a[i]), dfs(i + 1, 1 + j, score - a[i]))

	return dfs(0, 0, 0)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_score(n, m, a, b))
