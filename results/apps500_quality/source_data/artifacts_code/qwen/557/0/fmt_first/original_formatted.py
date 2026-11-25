def can_visit_friend(n, m, teleports):
    # Sort teleports by their starting position
    teleports.sort(key=lambda x: x[0])

    # Initialize the range [left, right] that Pig can reach
    left, right = 0, 0

    # Iterate through each teleport
    for a, b in teleports:
        # If the current teleport's starting position is beyond the current reachable range
        if a > right:
            return "NO"
        # Update the reachable range to the maximum limit of the current teleport
        right = max(right, b)

    # If the friend's house is within the reachable range
    if m <= right:
        return "YES"
    else:
        return "NO"


# Read input
n, m = map(int, input().split())
teleports = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_visit_friend(n, m, teleports))
