import sys

input = sys.stdin.read
data = input().split()

k = int(data[0])
n = int(data[1])
s = int(data[2])
p = int(data[3])

# Total number of sheets needed
total_sheets = k * n

# Number of sheets needed per person
sheets_per_person = n

# Number of packs needed
packs_needed = total_sheets // p

# If there is any remainder, we need an additional pack
if total_sheets % p != 0:
    packs_needed += 1

print(packs_needed)
