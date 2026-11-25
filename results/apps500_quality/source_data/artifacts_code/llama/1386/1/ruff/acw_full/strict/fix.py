

def solve():
	w, h = map(int, input().split())
	MOD = 998244353

	# Calculate the total number of possible tilings
	# The first tile can be rotated in 2 ways (white or black)
	total_ways = 2 ** (h * w)
	for i in range(1, w):
		total_ways = (total_ways + 2 ** (i * h)) % MOD
	print(total_ways % MOD)


if __name__ == "__main__":
	solve()
