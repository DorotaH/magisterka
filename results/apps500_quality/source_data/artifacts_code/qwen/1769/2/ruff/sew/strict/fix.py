def find_hill_stops(A, B):
    N=A+B+1
    stops=list(range(1, 1 + N))

    # Walk up the hill
    for i in range(A):
        stops[i], stops[1 + i]=stops[1 + i], stops[i]

    # Walk down the hill
    for i in range(A, A + B):
        stops[i], stops[1 + i]=stops[1 + i], stops[i]

    return  stops

# Read input
A, B = int(input()), int(input())

# Find and print the possible heights of the stops
print(' '.join(map(str, find_hill_stops(A, B))))
