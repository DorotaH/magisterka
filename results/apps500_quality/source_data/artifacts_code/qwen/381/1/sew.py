# Importing necessary libraries
import sys

# Reading input
k=int(sys.stdin.read().strip())

# Function to check if a k-regular graph with a bridge exists
def  construct_k_regular_graph_with_bridge(k):
    if not k == 1:
        n = 2 * k
        m = n - 1
        edges = []
        for i in range(1, n):
            edges.append((i, i + 1))
        edges.append((1, n))
        return "YES\n{} {}\n".format(n, m) + "\n".join("{} {}".format(a, b) for a, b in edges)
    else:
        return "NO"

# Output the result
result=construct_k_regular_graph_with_bridge(k)
sys.stdout.write(result)