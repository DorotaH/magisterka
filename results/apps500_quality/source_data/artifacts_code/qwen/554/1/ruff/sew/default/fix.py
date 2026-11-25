def  max_happiness(n, m, moods, subarrays):
    # Initialize a list to keep track of the number of chosen subarrays each flower is in
    flower_counts=[0]*n
    
    # Iterate over each subarray
    for  l, r in  subarrays:
        # Increment the count for each flower in the current subarray
        for  i in  range(l-1, r):
            flower_counts[i] += 1
    
    # Calculate the total happiness by summing the product of mood and number of chosen subarrays
    total_happiness=sum(flower_counts[i] * moods[i] for  i in  range(n))
    
    return  total_happiness

# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n, m = int(data[0]), int(data[1])
moods, subarrays = list(map(int, data[2:2+n])), [tuple(map(int, data[2+n+2*i:2+n+2*i+2])) for i in range(m)]

# Calculate and print the maximum happiness
print(max_happiness(n, m, moods, subarrays))
