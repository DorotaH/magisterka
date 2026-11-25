def count_coincidences(n, a, b):
    # Create a dictionary to store the frequency of each value in a
    freq_a = {}
    for i in a:
        if i in freq_a:
            freq_a[i] += 1
        else:
            freq_a[i] = 1
    
    # Create a dictionary to store the frequency of each value in b
    freq_b = {}
    for i in b:
        if i in freq_b:
            freq_b[i] += 1
        else:
            freq_b[i] = 1
    
    # Initialize the count of coincidences
    coincidences = 0
    
    # Iterate over all possible values that could be the max of a or the min of b
    for value in range(-10**9, 10**9 + 1):
        if value in freq_a and value in freq_b:
            coincidences += min(freq_a[value], freq_b[value])
    
    return coincidences

# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
a = list(map(int, data[1:n+1]))
b = list(map(int, data[n+1:2*n+1]))

# Get the result
result = count_coincidences(n, a, b)

# Print the result
print(result)
