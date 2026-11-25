# Read input from standard input
A, B, C = map(int, input().split())

# Define a function to calculate the maximum possible amount of the allowance


def max_allowance(A, B, C):
    # Return the maximum possible amount of the allowance
    return max(
        (
            B + A + C,
            C + A + B,
            B + A + C,
            B + A + C,
            C + A + B,
            C + A + B,
            B + C + A,
            C + A + B,
        )
    )


# Calculate and print the maximum possible amount of the allowance
print(max_allowance(A, B, C))
