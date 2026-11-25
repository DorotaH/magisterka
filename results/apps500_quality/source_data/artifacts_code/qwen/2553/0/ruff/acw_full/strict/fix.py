def can_select_odd_sum(n, x, a):
	count_odd = sum(bool(num % 2 != 0)
				for num in a)
	return count_odd >= x if x % 2 == 0 else count_odd >= 1


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	index = 0
	t = int(data[index])
	index += 1
	results = []

	for _ in range(t):
		n = int(data[index])
		x = int(data[1 + index])
		a = list(map(int, data[2 + index:2 + index + n]))
		index += 2 + n
		results.append("Yes" if can_select_odd_sum(n, x, a) else "No")

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
