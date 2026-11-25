def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	n = int(data[0])
	m = int(data[1])
	
	a = list(map(int, data[2:2 + n]))
	b = list(map(int, data[2 + n:2 + 2 * n]))
	
	queries = []
	index = 2 + 2 * n
	for _ in range(m):
		t = int(data[index])
		if t == 1:
			x = int(data[1 + index]) - 1
			y = int(data[2 + index]) - 1
			k = int(data[3 + index])
			queries.append((t, x, y, k))
			index += 4
		elif t == 2:
			x = int(data[1 + index]) - 1
			queries.append((t, x))
			index += 2
	
	for t, x, y, k in queries:
		if t == 1:
			for q in range(k):
				b[y + q] += a[q + x]
		elif t == 2:
			print(b[x])


if __name__ == "__main__":
	main()
