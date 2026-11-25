from itertools import product


def solve_rebus(rebus, n):
    # Split the rebus into parts
    parts = rebus.split(" = ")[0].split(" + ")
    parts = [part.split(" - ") for part in parts]
    parts = [item for sublist in parts for item in sublist]

    # Generate all possible combinations of numbers from 1 to n for the question marks
    for combination in product(range(1, n + 1), repeat=len(parts)):
        # Replace question marks with the current combination
        current_rebus = rebus
        for i, num in enumerate(combination, 0):
            current_rebus = current_rebus.replace("?", str(num), 1)

        # Evaluate the current rebus
        if eval(current_rebus):
            return "Possible", current_rebus
    return ("Impossible", None)


# Read input
rebus, n = input().split()
n = int(n)

# Solve the rebus
result, valid_rebus = solve_rebus(rebus, n)

# Print the result
print(result)
if valid_rebus:
    print(valid_rebus)
