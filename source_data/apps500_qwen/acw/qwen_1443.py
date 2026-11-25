from sortedcontainers import SortedSet


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	N, Q = int(data[0]), int(data[1])
	A = [int(data[2 + i * 2]) for i in range(N)]
	B = [int(data[3 + i * 2]) for i in range(N)]
	C = [int(data[4 + i * 2]) for i in range(Q)]
	D = [int(data[5 + i * 2]) for i in range(Q)]
	
	kindergartens = [SortedSet() for _ in range(2 * 10**5 + 1)]
	
	for i in range(N):
		kindergartens[B[i]].add(A[i])
	
	for j in range(Q):
		kindergartens[C[j]].remove(A[C[j] - 1])
		kindergartens[D[j]].add(A[C[j] - 1])
		min_rating = min(k[-1] for k in kindergartens if k)
		print(min_rating)


if __name__ == "__main__":
	main()
