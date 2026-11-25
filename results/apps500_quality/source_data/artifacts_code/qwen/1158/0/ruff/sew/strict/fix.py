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

# Calculate the minimum number of stolen utensils
# Each guest must have received a complete set of utensils
# The minimum number of utensils stolen is the number of utensils
# that are not part of a complete set for any guest
min_stolen = n

for utensil, count in utensil_count.items():
    # If the count is not a multiple of k, then some utensils of this type were stolen
    if  count % k != 0:
        min_stolen-=count%k

print(min_stolen)
