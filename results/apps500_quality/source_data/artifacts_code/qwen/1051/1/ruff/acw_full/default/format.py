def min_declined(K, ranks):
    # Initialize the list of invited contestants with the top 25 ranks
    invited = list(range(1, 26))

    # Convert the known ranks to a set for quick lookup
    known_ranks = set(ranks)

    return sum(bool(rank not in known_ranks) for rank in invited)


# Read input from standard input
K = int(input().strip())
ranks = list(map(int, input().strip().split()))

# Print the result
print(min_declined(K, ranks))
