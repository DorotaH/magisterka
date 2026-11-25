import sys
from collections import Counter

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
k = int(data[1])
remaining_utensils = list(map(int, data[2:]))

# Count the frequency of each utensil type
utensil_count = Counter(remaining_utensils)

min_stolen = n - sum(
    count % k for utensil, count in utensil_count.items() if count % k != 0
)
print(min_stolen)
