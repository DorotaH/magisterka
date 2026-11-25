def min_complexity(n, p):
    # Separate the bulbs into odd and even
    odd = [i for i in range(1, n+1) if i % 2 != 0]
    even = [i for i in range(1, n+1) if i % 2 == 0]
    
    # Initialize the complexity
    complexity = 0
    
    # Place the bulbs back on the garland
    i = 0
    j = 0
    for k in range(n):
        if p[k] == 0:
            if i < len(odd):
                p[k] = odd[i]
                i += 1
            else:
                p[k] = even[j]
                j += 1
                complexity += 1
    
    # Calculate the complexity
    for k in range(1, n):
        if p[k] % 2 != p[k-1] % 2:
            complexity += 1
    
    return complexity

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
p = list(map(int, data[1:]))

# Output the result
print(min_complexity(n, p))
