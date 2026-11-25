import sys
from collections import defaultdict
from typing import Dict


class UnionFind:
	def __init__(self):
		self.parent = {}
		self.rank = defaultdict(int)

	def find(self, x: str) -> str:
		if x not in self.parent:
			self.parent[x] = x
			self.rank[x] = 0
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, a: str, b: str):
		root_a, root_b = self.find(a), self.find(b)
		if root_a != root_b:
			if self.rank[root_b] < self.rank[root_a]:
				root_a, root_b = root_b, root_a
			self.parent[root_a] = root_b
			self.rank[root_b] += self.rank[root_a]
			return root_b
		return root_a


def main():
	n = int(sys.stdin.readline())
	passwords = [sys.stdin.readline().strip() for _ in range(n)]
	union = UnionFind()
	for password in passwords:
		for char in password:
			for other_password in passwords:
				if password != other_password:
					union.union(char, other_password)

	group_count = defaultdict(int)
	for password in passwords:
		group_count[union.find(password)] += 1

	max_group_count = max(group_count.values())
	print(max_group_count)


if __name__ == "__main__":
	main()
