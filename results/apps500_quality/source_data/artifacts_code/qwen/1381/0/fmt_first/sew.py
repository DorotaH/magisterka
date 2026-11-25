import sys

input = sys.stdin.read
data = input().split()

k, n = int(data[0]), int(data[1])
s, p = int(data[2]), int(data[3])

total_sheets_needed = n * k
packs_needed = (total_sheets_needed + p - 1) // p

print(packs_needed)