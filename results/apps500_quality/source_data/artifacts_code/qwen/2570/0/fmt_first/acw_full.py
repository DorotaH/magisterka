def can_rearrange(a, b, x):
	i = 0
	for ai in a:
		while i < len(b) and ai + b[i] > x:
			i += 1
		if i == len(b):
			return False
		i += 1
	return True


def solve():
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
		index += 2
		a = list(map(int, data[index : index + n]))
		index += n
		b = list(map(int, data[index : index + n]))
		index += n

		if can_rearrange(a, b, x):
			results.append("Yes")
		else:
			results.append("No")

	print("\n".join(results))


if __name__ == "__main__":
	solve()
