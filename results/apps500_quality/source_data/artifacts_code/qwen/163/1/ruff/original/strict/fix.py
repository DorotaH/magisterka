def can_reach_insect(n, k, line):
    grasshopper_pos = None
    insect_pos = None

    # Find the positions of the grasshopper and the insect
    for i in range(n):
        if line[i] == 'G':
            grasshopper_pos = i
        elif line[i] == 'T':
            insect_pos = i

    # Check if the positions are valid and calculate the difference
    if grasshopper_pos is None or insect_pos is None:
        return "NO"

    distance = abs(grasshopper_pos - insect_pos)

    # Check if the distance is divisible by k
    if distance % k == 0:
        return "YES"
    else:
        return "NO"

# Read input
n, k = map(int, input().split())
line = input().strip()

# Output the result
print(can_reach_insect(n, k, line))
