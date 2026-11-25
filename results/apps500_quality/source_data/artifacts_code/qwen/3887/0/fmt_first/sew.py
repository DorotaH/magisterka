def solve_rebus(rebus, n):
    from itertools import permutations

    # Extract the numbers from the rebus
    numbers = [int(x) for x in rebus.split() if x.isdigit()]
    variables = [i for i, x in enumerate(rebus.split()) if x == "?"]

    # Generate all possible permutations of numbers for the variables
    for perm in permutations(range(1, n + 1), len(variables)):
        # Replace the variables in the rebus with the permutation
        rebus_copy = rebus
        for  var, num in  zip(variables, perm):
            rebus_copy = rebus_copy.replace("?", str(num), 1)

        # Check if the rebus is valid
        if  eval(rebus_copy) == n:
            return  "Possible", rebus_copy

    return  "Impossible"


# Read input
rebus, n=input().split("=")
n=int(n)

# Solve the rebus
result, solution=solve_rebus(rebus, n)

# Print the result
print(result)
if result=="Possible":
    print(solution)