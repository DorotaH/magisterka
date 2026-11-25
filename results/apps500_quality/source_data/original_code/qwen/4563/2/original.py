from math import gcd

def min_votes(N, ratios):
    # Initialize the minimum votes for Takahashi and Aoki
    min_takahashi = 0
    min_aoki = 0
    
    # Iterate through the ratios to calculate the minimum possible total votes
    for i in range(N):
        t, a = ratios[i]
        # Calculate the least common multiple of the current ratio
        lcm = t * a // gcd(t, a)
        # Update the minimum votes for Takahashi and Aoki
        min_takahashi = max(min_takahashi, lcm * (i + 1) // (i + 1))
        min_aoki = max(min_aoki, lcm * (i + 1) // (i + 1))
    
    # Return the minimum possible total number of votes
    return min_takahashi + min_aoki

# Read input from standard input
N = int(input())
ratios = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the minimum possible total number of votes
print(min_votes(N, ratios))
