def count_ways_to_change(n, k, coefficients):
    # Calculate P(2)
    P_2 = sum(a * (2 ** i) for i, a in enumerate(coefficients))

    # Initialize the count of valid ways
    count = 0

    # Iterate over each coefficient and its position
    for i, a in enumerate(coefficients):
        # Calculate the required change to make P(2) = 0
        required_change = P_2

        # If the coefficient is not the leading coefficient, we need to adjust for x^i
        if i != n:
            required_change -= a * (2 ** i)

        # Calculate the possible new values for the coefficient
        for new_value in range(-k, k + 1):
            if k >= abs(new_value - a) and (new_value != coefficients[n] and (required_change + (2 ** i) * new_value) % (2 ** (i + 1)) == 0):
                count += 1

    return count


# Read input
n, k = map(int, input().split())
coefficients = list(map(int, input().split()))

# Print the result
print(count_ways_to_change(n, k, coefficients))
