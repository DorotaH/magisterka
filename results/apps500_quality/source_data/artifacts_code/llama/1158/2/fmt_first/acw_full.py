import sys


def minimum_stolen_utensils():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	max_count = max(a)
	max_count = max(max_count, k)

	return sum(max(0, max_count - a.count(i)) for i in range(1, 101))


sys.stdin.readline()  # Consume the newline left in input buffer
print(minimum_stolen_utensils())
