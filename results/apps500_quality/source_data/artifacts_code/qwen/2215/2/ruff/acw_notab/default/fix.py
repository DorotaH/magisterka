from collections import defaultdict


def maximize_beauty(n, m, visitors):
    # Initialize the count of roses and lilies in each segment
    roses = defaultdict(int)
    lilies = defaultdict(int)
    
    # Count the number of roses and lilies in each segment
    for l, r in visitors:
        for i in range(l, 1 + r):
            if i in roses:
                roses[i] += 1
            else:
                lilies[i] += 1
    
    # Determine the final arrangement
    result = []
    for i in range(1, 1 + n):
        if lilies[i] < roses[i]:
            result.append('0')  # Rose
        else:
            result.append('1')  # Lily
    
    return ''.join(result)


# Read input
n, m = map(int, input().split())
visitors = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(maximize_beauty(n, m, visitors))
