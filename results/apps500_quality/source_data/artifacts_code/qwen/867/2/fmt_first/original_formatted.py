# Read input
N = int(input())

# Calculate the minimum number of brains needed
# Heidi needs to get at least one brain, and she is the highest-ranked zombie
# She will vote for her own suggestion if it is at least as good as the best possible offer
# The best possible offer for Heidi is to get all the brains herself
# Therefore, the minimum number of brains needed is N
# If there are fewer than N brains, Heidi will not be able to get any brains
# If there are exactly N brains, Heidi can get one brain and all other brains will be left for the other zombies

print(N)
