from collections import defaultdict


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	index = 0
	n = int(data[index])
	m = int(data[1 + index])
	k = int(data[2 + index])
	index += 3

	a = []
	for _ in range(n):
		row = []
		for _ in range(m):
			row.append(int(data[index]))
			index += 1
		a.append(row)

	events = []
	for _ in range(k):
		x = int(data[index]) - 1
		y = int(data[1 + index]) - 1
		events.append((x, y))
		index += 2

	notification_count = [0] * n

	for x, y in events:
		for i in range(m):
			if a[x][i] == 1:
				notification_count[x] += 1

	for i in range(n):
		if a[i][y] == 1:
			notification_count[i] -= 1

	for i in range(n):
		if a[i][y] == 1:
			for j in range(m):
				if a[i][j] == 1:
					notification_count[i] -= 1

	for i in range(n):
		if a[i][y] == 1:
			for j in range(m):
				if a[i][j] == 1:
					for l in range(m):
						if a[i][l] == 1:
							notification_count[i] -= 1

	for i in range(n):
		if a[i][y] == 1:
			for j in range(m):
				if a[i][j] == 1:
					for l in range(m):
						if a[i][l] == 1:
							for p in range(m):
								if a[i][p] == 1:
									notification_count[i] -= 1

	print(" ".join(map(str, notification_count)))


if __name__ == "__main__":
	main()
