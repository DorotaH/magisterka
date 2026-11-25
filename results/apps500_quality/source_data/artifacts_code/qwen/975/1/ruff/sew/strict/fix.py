import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
sherlock_card = list(map(int, data[1]))
moriarty_card = list(map(int, data[2]))

# Calculate the minimum number of flicks Moriarty can get
min_flicks = 0
for s, m in zip(sherlock_card, moriarty_card):
    if  s != m:
        min_flicks += 1

# Calculate the maximum number of flicks Sherlock can get
max_flicks = 0
for s, m in zip(sherlock_card, moriarty_card):
    if  s != m:
        max_flicks += 1

print(min_flicks)
print(max_flicks)
