def can_visit_friend(n, m, teleports):
    # Create a set to store the points that can be reached
    reachable = set([0])

    # Process each teleport
    for teleport in teleports:
        # Get the location and limit of the teleport
        a, b = teleport

        # Get the points that can be reached by using this teleport
        new_reachable = set()
        for p in reachable:
            # If the point is within the teleport's range, add it to the new reachable set
            if p <= b:
                new_reachable.add(p)
                # If the point is the limit of the teleport, add all points to the right to the new reachable set
                if p == b:
                    new_reachable.update([i for i in range(a, b + 1)])

        # Update the reachable set
        reachable = reachable.union(new_reachable)

    # Return True if the friend's house is reachable, False otherwise
    return m in reachable


# Read input
n, m = map(int, input().split())
teleports = []
for _ in range(n):
    a, b = map(int, input().split())
    teleports.append((a, b))

# Print the result
print("YES" if can_visit_friend(n, m, teleports) else "NO")
