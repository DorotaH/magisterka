def maximize_score(a, b):
    if a == 0:
        return -b * b, "x" * b
    elif b == 0:
        return a * a, "o" * a
    else:
        return -1, "x" * b + "o" * a

# Read input
a, b = map(int, input().split())

# Get the maximum score and the corresponding arrangement
max_score, arrangement = maximize_score(a, b)

# Print the result
print(max_score)
print(arrangement)
