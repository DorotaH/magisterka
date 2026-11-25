def count_non_equal_modulo(a, b, l, r):
	# Calculate the number of integers x in the range [l, r] such that ((x % a) % b) != ((x % b) % a)
	# The modulo operation is periodic, so we can find the pattern within one period
	period = a * b
	return sum(bool(((x % a) % b) != ((x % b) % a))
		for x in range(l, 1 + r))


def main():
	import sys

	input = sys.stdin.read
	data = input().split()

	index = 0
	t = int(data[index])
	index += 1

	results = []
	for _ in range(t):
		a = int(data[index])
		b = int(data[1 + index])
		q = int(data[2 + index])
		index += 3

		test_case_results = []
		for _ in range(q):
			l = int(data[index])
			r = int(data[1 + index])
			index += 2
			result = count_non_equal_modulo(a, b, l, r)
			test_case_results.append(result)

		results.extend(test_case_results)

	for result in results:
		print(result, end=" ")
	print()


if __name__ == "__main__":
	main()
