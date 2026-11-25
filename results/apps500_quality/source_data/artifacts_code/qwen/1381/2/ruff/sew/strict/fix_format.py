import sys

input = sys.stdin.read
data = input().split()

k, n = int(data[0]), int(data[1])
s, p = int(data[2]), int(data[3])

# Total number of sheets needed
total_sheets = n * k

# Number of sheets needed per person
sheets_per_person = n

# Number of packs needed
packs_needed = total_sheets // p

# If there is any remainder, we need an additional pack
if total_sheets % p != 0:
    packs_needed = packs_needed + 1

print(packs_needed)
