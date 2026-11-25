# Solution to the problem
def min_brains(N):
    # For N = 1, Heidi must take the only brain available
    if N == 1:
        return 1
    # For N > 1, Heidi needs to ensure she gets at least one brain and that half of the votes are in her favor
    # The optimal strategy for Heidi is to offer one brain to herself and one to the lowest-ranked zombie
    # This ensures that she gets one brain and half of the votes (including her own)
    return 2

# Read input
N = int(input().strip())

# Output the result
print(min_brains(N))
