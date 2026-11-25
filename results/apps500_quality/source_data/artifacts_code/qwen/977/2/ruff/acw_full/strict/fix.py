

def count_valid_permutations(n: int, a: list[int]) -> int:
	# Sort the array a to simplify the problem
	a.sort()

	return sum(bool(all(x >= a[i] for i in range(n)))
		for x in range(1, 1 + n))


def find_good_integers(n: int, p: int, a: list[int]) -> list[int]:
	# Count the number of valid permutations for each x
	valid_counts = [count_valid_permutations(n, a[:i]) for i in range(1, 1 + n)]

	return [x for x, count in enumerate(valid_counts, start=1) if count % p != 0]


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	n = int(data[0])
	p = int(data[1])
	a = list(map(int, data[2:]))

	good_integers = find_good_integers(n, p, a)

	print(len(good_integers))
	print(' '.join(map(str, good_integers)))


if __name__ == "__main__":
	main()
