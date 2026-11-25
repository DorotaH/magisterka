from  fractions import  Fraction
from  math import  gcd

def min_votes(N, ratios):
    # Initialize the current number of votes for Takahashi and Aoki
    takahashi = 1
    aoki = 1
    
    # Iterate through the ratios from the second to the last
    for i in range(1, N):
        t, a = ratios[i]
        # Calculate the greatest common divisor of the current and new ratios
        g = gcd(t, a)
        # Update the number of votes for Takahashi and Aoki
        takahashi *= t // g
        aoki *= a // g
    
    # Return the total number of votes
    return takahashi + aoki

# Read input
N = int(input())
ratios = []
for _ in range(N):
    ratios.append(tuple(map(int, input().split())))

# Print the result
print(min_votes(N, ratios))
