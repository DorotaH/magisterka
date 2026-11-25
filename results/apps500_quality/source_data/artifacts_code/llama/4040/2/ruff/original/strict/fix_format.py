def reach_platforms(n, m, d, c):
    # Sort the platforms by their end positions
    c = sorted((c[i], i + 1) for i in range(m))

    # Initialize the end position of the current platform
    end = 0

    # Initialize the answer array
    a = [0] * (n + 1)

    # Iterate over the platforms
    for i in range(m):
        # If the current platform can be reached from the previous platform
        if c[i][0] - 1 - end >= d:
            # Add the current platform to the answer array
            a[end + 1 : end + c[i][0]] = [c[i][1]] * c[i][0]
            # Update the end position of the current platform
            end = c[i][0]
        # If the current platform cannot be reached from the previous platform
        else:
            # If the current platform can be reached from the previous platform with a jump
            if c[i][0] - 1 - end <= d:
                # Add the current platform to the answer array
                a[0 : c[i][0]] = [c[i][1]] * c[i][0]
                # Update the end position of the current platform
                end = c[i][0]
            # If the current platform cannot be reached
            else:
                return "NO"

    # If the last platform cannot be reached
    if end < n:
        return "NO"

    # Return the answer
    return "YES\n" + " ".join(map(str, a[1:-1]))


# Read the input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Print the output
print(reach_platforms(n, m, d, c))
