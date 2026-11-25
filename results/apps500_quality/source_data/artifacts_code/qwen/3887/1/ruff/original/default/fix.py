def solve_rebus(rebus, n):
    # Split the rebus into parts based on '='
    parts = rebus.split(' = ')
    left_side = parts[0]
    right_side = int(parts[1])
    
    # Split the left side into individual terms
    terms = left_side.split(' + ')
    terms = [term.split(' - ') for term in terms]
    
    # Flatten the list of terms
    terms = [item for sublist in terms for item in sublist]
    
    # Try to find a combination of numbers that satisfy the equation
    from itertools import permutations
    
    for perm in permutations(range(1, n+1), len(terms)):
        if eval(' + '.join(map(str, perm)).replace(' - ', ' -')) == right_side:
            result = ' + '.join(map(str, perm)).replace(' - ', ' -')
            return "Possible\n" + result + " = " + str(right_side)
    
    return "Impossible"

# Read input from standard input
import sys

rebus = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

# Solve the rebus and print the result
result = solve_rebus(rebus, n)
print(result)
