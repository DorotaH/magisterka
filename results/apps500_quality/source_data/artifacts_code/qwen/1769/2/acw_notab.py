def find_hill_stops(A, B):
    N = B + A + 1
    stops = list(range(1, N + 1))
    
    # Walk up the hill
    for i in range(A):
        stops[i], stops[i + 1] = stops[i + 1], stops[i]
    
    # Walk down the hill
    for i in range(A, B + A):
        stops[i], stops[i + 1] = stops[i + 1], stops[i]
    
    return stops


# Read input
A = int(input())
B = int(input())

# Find and print the possible heights of the stops
print(' '.join(map(str, find_hill_stops(A, B))))
