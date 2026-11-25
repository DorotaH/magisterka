import sys

# Read the number of onsite finalists
K = int(sys.stdin.readline().strip())

# Read the ranks of the onsite finalists
ranks = list(map(int, sys.stdin.readline().strip().split()))

# Sort the ranks in ascending order
ranks.sort()

# Initialize the total declined contestants and the current rank
declined = 0
current_rank = 1

# Iterate over the ranks of the onsite finalists
for r in ranks:
    # If the current rank is not equal to the rank of the onsite finalist, increment the declined contestants and the current rank
    if r != current_rank:
        declined = declined + 1
        current_rank = current_rank + 1

# Calculate the minimum possible number of declined contestants
declined += 25 - K

print(declined)
