# Solution for the problem

# Read input
k = int(input())

# Check if such a graph exists
if k == 1:
	print("NO")
else:
	print("YES")
	n = 2 * k  # Number of vertices
	m = n - 1  # Number of edges
	print(n, m)
	# Create a cycle graph with a bridge
	for i in range(1, n):
		print(i, i + 1)
	print(1, n)
