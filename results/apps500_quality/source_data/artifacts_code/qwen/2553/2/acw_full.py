import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
	n = int(data[index])
	x = int(data[1 + index])
	a = list(map(int, data[2 + index:2 + index + n]))
	index += 2 + n
	
	# Count the number of odd numbers in the array
	odd_count = sum(bool(num % 2 != 0)
				for num in a)
	
	# Check if it's possible to select x elements such that their sum is odd
	if odd_count >= x:
		results.append("Yes")
	else:
		results.append("No")

# Print all results
for result in results:
	print(result)
