def min_complexity(n, p):
    # Separate the bulbs into even and odd
    even = [i for i in range(1, n + 1) if i % 2 == 0]
    odd = [i for i in range(1, n + 1) if i % 2 != 0]
    
    # Initialize the garland with the first bulb
    garland=[p[0]]
    
    # Place the bulbs back on the garland
    for i in range(1, n):
        if  p[i] == 0:
            if not garland[-1] % 2 == 0:
                garland.append(even.pop(0))
            else:
                garland.append(odd.pop(0))
    
    # Calculate the complexity
    complexity=0
    for i in range(1, n):
        if  garland[i]%2!=garland[i-1]%2:
            complexity = complexity + 1
    
    return  complexity

# Read input
import sys
input=sys.stdin.read
data=input().split()
n, p = int(data[0]), list(map(int, data[1:]))

# Output the result
print(min_complexity(n, p))