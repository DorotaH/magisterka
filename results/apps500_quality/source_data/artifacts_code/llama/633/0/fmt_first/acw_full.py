import sys


def read_ints():
	return map(int, sys.stdin.readline().split())


def read_int():
	return int(sys.stdin.readline())


n, m = read_ints()

if m < n - 1 or (m == n - 1 and n % 2 == 0):
	print("Possible")
	if m == n - 1:
		for i in range(1, n):
			print(f"{i} {i + 1}")
	else:
		for i in range(1, m):
			print(f"{i * 2} {i * 2 + 1}")
		for i in range(1, n - (m - (m % 2)) // 2):
			print(f"{i} {i + 1}")
elif m > (n - 2) * (n - 1) // 2:
	print("Impossible")
else:
	print("Possible")
	for i in range(1, m):
		print(f"{i * 2} {i * 2 + 1}")
	for i in range(1, n - m):
		print(f"{i} {i + 1}")
