import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))


# Function to check if a number divides another number
def divides(x, y):
	return x % y == 0


# Function to count numbers that satisfy the condition
def count_valid_numbers(N, A):
	count = 0
	for i in range(N):
		valid = not any(i != j and divides(A[j], A[i]) for j in range(N))
		if valid:
			count += 1
	return count


# Output the result
print(count_valid_numbers(N, A))
