from fractions import Fraction
from sys import stdin

input = stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:]))

# Convert concentrations to fractions for exact arithmetic
a = [Fraction(a_i, 1000) for a_i in a]

# Target concentration
target = Fraction(n, 1000)

# Find the minimal volume to achieve the target concentration


def find_min_volume(a, target):
    from collections import defaultdict
    from heapq import heappush, heappop

    # Dictionary to store the minimum volume for each concentration
    min_volumes = defaultdict(lambda: float("inf"))
    min_volumes[Fraction(0)] = 0

    # Priority queue to store the current concentration and volume
    pq = [(Fraction(0), 0)]

    while pq:
        current_concentration, current_volume = heappop(pq)

        # If we found the target concentration, return the volume
        if current_concentration == target:
            return current_volume

        # If the current volume is already larger than the minimum volume for this concentration, skip it
        if min_volumes[current_concentration] <= current_volume:
            continue

        # Update the minimum volume for this concentration
        min_volumes[current_concentration] = current_volume

        # Try adding each type of Coke
        for a_i in a:
            new_concentration = current_concentration + a_i
            new_volume = 1 + current_volume
            heappush(pq, (new_concentration, new_volume))

    # If we exhaust the priority queue without finding the target concentration, return -1
    return -1


# Print the result
print(find_min_volume(a, target))
