def main():
	import sys
	from bisect import bisect_left
	input = sys.stdin.readline

	N = int(input())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	C = [a - b for a, b in zip(A, B)]
	C.sort()

	ans = 0
	for i, c in enumerate(C):
		j = bisect_left(C, 1 + -c)
		ans += N - j
		if 0 < c:
			ans -= 1
	print(ans // 2)


def __starting_point():
	main()


__starting_point()
