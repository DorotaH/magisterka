# Read input
import sys

input = sys.stdin.read
data = input().split()

# Number of test cases
T = int(data[0])

# Initialize index for reading data
index = 1

# Output the results
results = []
for _ in range(T):
	n = int(data[index])
	index += 1
	
	# Calculate the minimum number of turns
	if n % 2 == 0:
		# If n is even, the minimum number of turns is n/2
		results.append(n // 2)
	else:
		# If n is odd, the minimum number of turns is (n+1)/2
		results.append((1 + n) // 2)

# Print all results
print('\n'.join(map(str, results)))
