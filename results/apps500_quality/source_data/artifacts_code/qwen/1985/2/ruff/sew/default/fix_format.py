def find_initial_scores(k, n, a, b):
    # Initialize the set of possible initial scores
    possible_scores = set()

    # Sort the jury marks and the remembered scores
    a.sort()
    b.sort()

    # Iterate over all possible initial scores
    for initial in range(-4_000_000, 4_000_001):
        # Calculate the scores after each jury member's rating
        current_score = initial
        valid = True
        for mark in a:
            current_score += mark
            if current_score not in b:
                valid = False
                break
        # If all marks are valid, add the initial score to the set
        if valid:
            possible_scores.add(initial)

    # Return the number of possible initial scores
    return len(possible_scores)


# Read input
k, n = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

# Find and print the number of options for the initial score
print(find_initial_scores(k, n, a, b))
