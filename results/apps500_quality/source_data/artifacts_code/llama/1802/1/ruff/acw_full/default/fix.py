def solve():
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	min_val = arr[0]
	max_buns = 0
	step = 0
	for i in range(n):
		if i != 0:
			if abs(arr[i]) > abs(arr[i - 1]):
				arr[i] -= abs(arr[i - 1]) - abs(arr[i])
			elif abs(arr[i]) < abs(arr[i - 1]):
				arr[i] += abs(arr[i - 1]) - abs(arr[i])
				max_buns += abs(arr[i - 1]) - abs(arr[i])
			else:
				pass
		max_buns = max(max_buns, max(abs(arr[i]), abs(arr[i - 1])))
	print(max_buns)
	print(min_val, int((arr[n - 1] - min_val) / (n - 1)))


solve()
