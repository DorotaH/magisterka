def can_grasshopper_reach_insect(n, k, line):
    # Find the positions of the grasshopper and the insect
    grasshopper_pos = line.find('G')
    insect_pos = line.find('T')

    # Calculate the absolute difference between their positions
    distance = abs(grasshopper_pos - insect_pos)

    # Check if the distance is a multiple of k
    return "YES" if distance % k == 0 else "NO"


# Read input
n, k = map(int, input().split())
line = input().strip()

# Output the result
print(can_grasshopper_reach_insect(n, k, line))
