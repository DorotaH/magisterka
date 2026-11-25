

def solve():
	a = list(map(int, input().split()))
	n = int(input())
	b = list(map(int, input().split()))

	freq = 6 * [0]
	used = False

	min_fret = float('inf')
	max_fret = float('-inf')

	for i in range(n):
		for j in range(6):
			if b[i] <= a[j] + 10**9:
				freq[j] += 1
				used = True
				max_fret = max(max_fret, b[i] - a[j])
				min_fret = min(min_fret, b[i] - a[j])
				break

	if not used:
		max_fret = b[-1]
		min_fret = 0

	print(max_fret - min_fret)


if __name__ == '__main__':
	solve()
