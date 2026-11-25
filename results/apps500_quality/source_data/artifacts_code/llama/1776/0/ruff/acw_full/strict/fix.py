from functools import lru_cache


def solve(expression, n_plus, n_minus):
	@lru_cache(None)
	def dfs(i, n_plus, n_minus):
		if n_plus == 0 and n_minus == 0:
			return int(expression[i:])

		if i == len(expression) - 1:
			return 0

		max_val = float('-inf')
		min_val = float('inf')
		for j in range(i, len(expression)):
			if expression[j] == '?':
				if n_plus > 0:
					max_val = max(max_val, dfs(i, n_plus - 1, n_minus) + dfs(1 + j, n_plus, n_minus))
					min_val = min(min_val, dfs(i, n_plus - 1, n_minus) - dfs(1 + j, n_plus, n_minus))
				if n_minus > 0:
					max_val = max(max_val, dfs(i, n_plus, n_minus - 1) - dfs(1 + j, n_plus, n_minus))
					min_val = min(min_val, dfs(i, n_plus, n_minus - 1) + dfs(1 + j, n_plus, n_minus))

			if expression[j] != '?':
				if expression[j] == '(':
					n_plus += 1
				elif expression[j] == ')':
					n_plus -= 1

		return max_val if n_plus >= 0 else float('-inf')
	return dfs(0, n_plus, n_minus)


def main():
	expression = input()
	n_plus, n_minus = map(int, input().split())
	print(solve(expression, n_plus, n_minus))


if __name__ == "__main__":
	main()
