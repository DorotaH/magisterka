import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

# Function to calculate the minimum number of moves to reach a square containing N


def min_moves(N):
	# The minimum number of moves is the sum of the exponents in the prime factorization of N
	count = 0
	for i in range(2, N + 1):
		while N % i == 0:
			count += 1
			N //= i
	return count


# Output the result
print(min_moves(N))
