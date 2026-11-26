def find_possible_parents(n, edges):
    # Initialize the parent array with -1
    parent = [-1] * (pow(2, n) - 1)
    # Initialize the degree array with 0
    degree = [0] * (pow(2, n) - 1)

    # Set the parent for the root node
    parent[0] = -1

    # Populate the degree array and set the parent for each node
    for a, b in edges:
        degree[a - 1] += 1
        degree[b - 1] += 1
        parent[b - 1] = a - 1

    # Find all leaf nodes (nodes with degree 1)
    leaf_nodes = [i for i in range(1, pow(2, n) - 1) if 1 == degree[i]]

    # Check if all leaf nodes have the same parent
    if not len(set(parent[i] for i in leaf_nodes)) == 1:
        return 0, []
    else:
        return 1, [parent[leaf_nodes[0]]]


# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(2**n - 3)]

# Find possible parents
num_answers, possible_parents = find_possible_parents(n, edges)

# Print the output
print(num_answers)
if possible_parents:
    print(" ".join(map(str, possible_parents)))
