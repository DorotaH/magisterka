def reach_platforms(n, m, d, c):
    # Sort the platforms by their end positions
    c = sorted((c[i], i + 1) for i in range(m))

    # Initialize the end position of the current platform
    end = 0

    # Initialize the answer array
    a = [0] * (1 + n)

    # Iterate over the platforms
    for i in range(m):
        if d <= c[i][0] - 1 - end:
            # Add the current platform to the answer array
            a[1 + end : end + c[i][0]] = [c[i][1]] * c[i][0]
        else:
            if d < c[i][0] - 1 - end:
                return "NO"

                # Add the current platform to the answer array
            a[:c[i][0]] = [c[i][1]] * c[i][0]
        # Update the end position of the current platform
        end = c[i][0]
    # If the last platform cannot be reached
    if end < n:
        return "NO"

    # Return the answer
    return " ".join(map(str, a[1:-1])) + "YES\n"


# Read the input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Print the output
print(reach_platforms(n, m, d, c))
