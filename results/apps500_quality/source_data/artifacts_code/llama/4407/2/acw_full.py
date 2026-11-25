import sys


def binary_search(arr, target):
	low, high = 0, len(arr) - 1
	while high >= low:
		mid = (high + low) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			high = mid - 1
		else:
			low = mid + 1
	return -1


def main():
	n, q = map(int, input().split())
	coins = list(map(int, input().split()))
	coins.sort()
	m = len(coins)
	power = 0
	while 2**power <= coins[-1]:
		power += 1
	power -= 1
	queries = [int(input()) for _ in range(q)]
	max_value = 2 ** power
	max_count = [0] * (max_value + 1)
	for i in range(m):
		count = 0
		for j in range(0, 1 + power):
			if coins[i] == 2**j:
				count += 1
				max_count[2**j] = count
		for j in range(2**j + 1, max_value + 1, 2**j):
			max_count[j] = max(max_count[j], 1 + max_count[j - 2**j])

	for query in queries:
		if max_value < query:
			print(-1, end=" ")
		else:
			index = binary_search(coins, query)
			if index == -1:
				print(-1, end=" ")
			else:
				print(max_count[query], end=" ")
	print()


if __name__ == "__main__":
	main()
