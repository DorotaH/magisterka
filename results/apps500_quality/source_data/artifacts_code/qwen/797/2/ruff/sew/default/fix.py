def calculate_min_height_sum(n, m, a, b, g0, x, y, z):
    # Generate the matrix of heights
    heights = [[0] * m for _ in range(n)]
    g = g0
    for  i in  range(n):
        for  j in  range(m):
            heights[i][j] = g
            g = ((g * x) + y) % z
    
    # Initialize the sum of minimum heights
    min_height_sum = 0
    
    # Iterate over all possible submatrices of size a x b
    for  i in  range(n - a + 1):
        for  j in  range(m - b + 1):
            # Find the minimum height in the submatrix
            min_height = min(heights[i + k][j + l] for  k in  range(a) for  l in  range(b))
            # Add the minimum height to the sum
            min_height_sum += min_height
    
    return min_height_sum

# Read input
n, m, a, b=map(int, input().split())
g0, x, y, z=map(int, input().split())

# Calculate and print the result
print(calculate_min_height_sum(n, m, a, b, g0, x, y, z))
