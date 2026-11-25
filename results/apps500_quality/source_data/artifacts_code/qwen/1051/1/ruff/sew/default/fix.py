def min_declined(K, ranks):
    # Initialize the list of invited contestants with the top 25 ranks
    invited=list(range(1, 26))
    
    # Convert the known ranks to a set for quick lookup
    known_ranks=set(ranks)
    
    # Iterate over the invited list and count the number of decliners
    declined_count=0
    for rank in invited:
        if rank not in known_ranks:
            declined_count += 1
    
    return declined_count

# Read input from standard input
K = int(input().strip())
ranks = list(map(int, input().strip().split()))

# Print the result
print(min_declined(K, ranks))
