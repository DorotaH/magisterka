from collections import Counter


def check(t, freq, min_val, max_val):
	"""Check if it's possible to end up with t."""
	return 2 <= freq[t] or (freq[t] == 1 and min_val <= t <= max_val)


def main():
	n, q = map(int, input().split())
	A = sorted(map(int, input().split()))
	freq = Counter(A)

	for _ in range(q):
		t = int(input())
		min_val = A[0]
		max_val = A[-1]
		print('Yes' if check(t, freq, min_val, max_val) else 'No')


if __name__ == "__main__":
	main()
