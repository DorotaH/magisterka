import math

k, n, s, p = map(int, input().split())

# Calculate the total number of sheets each person needs
sheets_per_person = n * s

# Calculate the total number of sheets needed
total_sheets_needed = k * sheets_per_person

# Calculate the minimum number of packs needed
min_packs = math.ceil(total_sheets_needed / p)

print(min_packs)
