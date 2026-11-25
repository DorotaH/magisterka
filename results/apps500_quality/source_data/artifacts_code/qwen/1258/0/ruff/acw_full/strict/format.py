from collections import defaultdict


def reconstruct_permutation(n, triples):
    # Create a dictionary to store the triples
    triple_dict = defaultdict(list)
    for i, (a, b, c) in enumerate(triples):
        triple_dict[a].append((i, 0))
        triple_dict[b].append((i, 1))
        triple_dict[c].append((i, 2))

    # Sort the triples by the first element
    for key in triple_dict:
        triple_dict[key].sort()

    # Create a list to store the permutation
    perm = [0] * n

    # Iterate through the sorted triples
    for key in triple_dict:
        for i, pos in triple_dict[key]:
            perm[i + pos] = key

    return perm


# Read input
n = int(input())
triples = [tuple(map(int, input().split())) for _ in range(n - 2)]

# Reconstruct the permutation
perm = reconstruct_permutation(n, triples)

# Print the permutation
print(" ".join(map(str, perm)))
