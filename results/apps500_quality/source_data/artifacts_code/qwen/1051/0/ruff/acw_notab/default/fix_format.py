def min_declined(K, ranks):
    # The initial list of invited contestants is the first K ranks in ascending order
    invited = sorted(ranks)
    # The total number of contestants that could have been invited is from rank 1 to rank 10^6
    total_invited = list(range(1, 10**6 + 1))
    # The number of contestants that declined is the difference between the total invited and the actually invited
    declined = [x for x in total_invited if x not in invited]
    return len(declined)


# Read input
K = int(input())
ranks = list(map(int, input().split()))

# Output the result
print(min_declined(K, ranks))
