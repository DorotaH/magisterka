import sys


def process_changes(n: int, a: list[int], q: int, changes: list[list[int]]) -> list[int]:
	def balance_sequence(a: list[int]) -> list[int]:
		b = [a[0]]
		for i in range(1, n):
			b.append(max(b[-1], a[i]))
		return b

	def get_min_max(b: list[int], c: list[int]) -> int:
		return max(max(b), max(c))

	b = balance_sequence(a)
	c = [a[-1]] * n
	results = [get_min_max(b, c)]

	for l, r, x in changes:
		for i in range(l - 1, r):
			a[i] += x
		b = balance_sequence(a)
		c = [a[-1]] * n
		results.append(get_min_max(b, c))

	return results


def main():
	input = sys.stdin.read
	data = input().split()

	n = int(data[0])
	a = list(map(int, data[1:1 + n]))
	q = int(data[1 + n])
	changes = []
	for i in range(q):
		l = int(data[2 + n + i * 3]) - 1
		r = int(data[3 + n + i * 3]) - 1
		x = int(data[4 + n + i * 3])
		changes.append([l, r, x])

	results = process_changes(n, a, q, changes)
	for result in results:
		print(result)


if __name__ == "__main__":
	main()
