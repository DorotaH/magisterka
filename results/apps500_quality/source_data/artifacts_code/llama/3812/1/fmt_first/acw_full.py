import sys


def solve():
	s = input().strip()
	t = input().strip()
	n, m = len(s), len(t)
	operations = []
	i, j = 0, 0
	while i < n and m > j:
		if s[i] == t[j]:
			i += 1
			j += 1
		elif s[i] == "a":
			operations.append((i, j))
			i += 1
			j += 1
		else:
			operations.append((n - i, m - j))
			i += 1
	while i < n:
		operations.append((n - i, m))
		i += 1
	while m > j:
		operations.append((i, m - j))
		j += 1
	print(len(operations))
	for i in range(len(operations)):
		print(*operations[i])


def main():
	solve()


if __name__ == "__main__":
	main()
