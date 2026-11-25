import sys
from collections import defaultdict


def solve():
	n = int(input())
	a = list(map(int, input().split()))
	m = max(a)  # max element in the array
	last = [-1] * (1 + m)  # store last index of each element

	# store the last index of each element
	for i in range(n):
		last[a[i]] = i

	ans = 1  # the subpermutation of a single element
	for i in range(2, 1 + m):
		# if i is not present in the array, we have 0 subpermutations
		if last[i] == -1:
			continue

		# the number of subpermutations ending at index i
		# is the product of the number of subpermutations ending at last[i] and (i - last[i])
		ans *= (last[i] - last[i - 1] - 1) * (last[i] - last[i - 1])

	print(ans)


if __name__ == "__main__":
	solve()
