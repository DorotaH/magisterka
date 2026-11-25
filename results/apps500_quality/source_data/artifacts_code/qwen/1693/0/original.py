def optimal_skyscrapers(n, m):
    # Initialize the result list with zeros
    a = [0] * n
    
    # Iterate through each plot
    for i in range(n):
        # Set the number of floors to the minimum of m_i and the maximum possible value
        a[i] = min(m[i], n - i)
    
    return a

# Read input
n = int(input())
m = list(map(int, input().split()))

# Get the optimal number of floors for each skyscraper
result = optimal_skyscrapers(n, m)

# Print the result
print(" ".join(map(str, result)))
