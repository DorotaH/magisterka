#!/usr/bin/env python3
def main():
	M, K = map(int, input().split())
	if K == 0:
		print(*[i // 2 for i in range(2 ** (1 + M))])
	elif K >= 2**M or 1 >= M:
		print(-1)
	else:
		nums = [i for i in range(2**M) if i != K]
		a = [nums[0], K, nums[0]]
		b = [nums[i] for i in range(1, 2**M - 1)]
		b.append(K)
		b.extend(nums[2**M - 1 - i] for i in range(1, 2**M - 1))
		print(*a, *b)


def __starting_point():
	main()


__starting_point()
