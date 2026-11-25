def can_grasshopper_reach_insect(n, k, line):
    start = line.index("G")
    target = line.index("T")

    # Check if the start and target are within the same segment of length 2k
    if abs(start - target) <= k * 2:
        # Check if there are no obstacles in the way
        if all(
            line[i] != "#" for i in range(min(start, target), max(start, target) + 1)
        ):
            return "YES"
    return "NO"


# Read input
n, k = map(int, input().split())
line = input().strip()

# Output the result
print(can_grasshopper_reach_insect(n, k, line))
