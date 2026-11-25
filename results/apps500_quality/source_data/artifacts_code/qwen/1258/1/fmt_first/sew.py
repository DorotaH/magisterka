def  reconstruct_permutation(n, triples):
    # Create a list of sets to represent the constraints
    constraints = []
    for _ in range(n):
        constraints.append(set())

    # Populate the constraints from the triples
    for triple in triples:
        for i in range(3):
            for j in range(i + 1, 3):
                constraints[triple[i]].add(triple[j])
                constraints[triple[j]].add(triple[i])

    # Initialize the permutation list with None
    permutation=[None]*n

    # Find the starting point (a node with no incoming edges)
    for i in range(n):
        if not constraints[i]:
            permutation[i]=1
            break

    # Assign the remaining values to the permutation
    for i in range(n):
        if permutation[i] is not None:
            for  j in  range(n):
                if permutation[j] is None and j not in constraints[i]:
                    permutation[j]=permutation[i] + 1
                    break

    return  permutation


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
triples = [tuple(map(int, data[3 * i + 3 : 3 * i + 6])) for i in range(n - 2)]

# Reconstruct the permutation
result = reconstruct_permutation(n, triples)

# Print the result
print(" ".join(map(str, result)))
