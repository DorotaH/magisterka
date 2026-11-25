from  collections import  defaultdict
from  itertools import  combinations_with_replacement

MOD=998244353


def count_combinations(K, N):
    # Initialize a dictionary to store the count of combinations for each sum
    count=defaultdict(int)
    
    # Iterate over all possible combinations of N sides from K-sided dice
    for combo in combinations_with_replacement(range(1, K+1), N):
        # Calculate the sum of the current combination
        current_sum=sum(combo)
        # If the sum is greater than 2K, we are only interested in sums up to 2K
        if  current_sum>K*2:
            continue
        # Increment the count for this sum
        count[current_sum]+=1
    
    # Return the counts for sums from 2 to 2K
    return  [count[i] for  i in  range(2, 2*K+1)]

# Read input from standard input
K, N=map(int, input().split())

# Get the counts of valid combinations
result=count_combinations(K, N)

# Print the result
for  num in  result:
    print(num)