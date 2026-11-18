class Solver:
	def __init__(self):
		pass

	def solve(self):
		n, t, k, d = list(map(int, input().split()))
		n = (k + n - 1) // k
		if d < t * (n - 1):
			print("YES")
		else:
			print("NO")


def __starting_point():
	s = Solver()
	s.solve()


__starting_point()
