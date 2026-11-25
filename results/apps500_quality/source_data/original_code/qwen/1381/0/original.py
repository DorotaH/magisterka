import sys
input = sys.stdin.read
data = input().split()

k = int(data[0])
n = int(data[1])
s = int(data[2])
p = int(data[3])

total_sheets_needed = k * n
packs_needed = (total_sheets_needed + p - 1) // p

print(packs_needed)
