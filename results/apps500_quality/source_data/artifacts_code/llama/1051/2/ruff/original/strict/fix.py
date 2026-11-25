
def min_declined(k, r):
    """Return the minimum number of contestants that declined the invitation to compete onsite in the final round."""

    # Sort the list of ranks in ascending order
    r.sort()

    # Initialize a set to keep track of invited contestants
    invited = set(r)

    # Initialize a variable to keep track of the number of declined contestants
    declined = 0

    # Iterate over all possible ranks
    for i in range(1, 1000001):
        # If the current rank is not in the invited set, increment the declined count and add it to the invited set
        if i not in invited:
            declined += 1
            invited.add(i)
        # If the number of invited contestants reaches 25, break the loop
        if len(invited) == k:
            break

    # Return the minimum number of declined contestants
    return declined - len(invited)


# Read the input from standard input
k = int(input())
r = list(map(int, input().split()))

# Print the answer to standard output
print(min_declined(k, r))
