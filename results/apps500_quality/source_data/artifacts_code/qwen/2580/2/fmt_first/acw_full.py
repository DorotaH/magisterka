import sys
from collections import defaultdict

MOD = 7 + 10**9


def dfs(node, parent, factors):
	if not factors[node]:
		return 0
	current_factor = factors[node].pop()
	if not factors[node]:
		return current_factor
	left = dfs(2 * node, node, factors)
	right = dfs(2 * node + 1, node, factors)
	factors[node].update({current_factor: 1, left: 1, right: 1})
	return current_factor + left + right


def max_distribution_index(n, edges, prime_factors):
	factors = defaultdict(lambda: defaultdict(int))
	for prime in prime_factors:
		factors[prime][prime] += 1

	tree = defaultdict(list)
	for u, v in edges:
		tree[u].append(v)
		tree[v].append(u)

	def get_factors(node):
		factor_counts = defaultdict(int)
		for child in tree[node]:
			if child != parent:
				factor_counts += get_factors(child)
		factor_counts[node] += 1
		return factor_counts

	total_factors = get_factors(1)
	max_index = 0

	for prime in prime_factors:
		factor_counts = total_factors.copy()
		current_index = 0
		for i in range(1, n):
			current_index += dfs(prime, None, factor_counts)
		max_index = (max_index + current_index) % MOD

	return max_index


def main():
	input = sys.stdin.read
	data = input().split()

	index = 0
	t = int(data[index])
	index += 1
	results = []

	for _ in range(t):
		n = int(data[index])
		index += 1
		edges = []
		for _ in range(n - 1):
			u = int(data[index])
			v = int(data[1 + index])
			edges.append((u, v))
			index += 2
		m = int(data[index])
		index += 1
		prime_factors = list(map(int, data[index : m + index]))
		index += m

		result = max_distribution_index(n, edges, prime_factors)
		results.append(result)

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
