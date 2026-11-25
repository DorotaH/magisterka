import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
sherlock_card = list(map(int, data[1]))
moriarty_card = list(map(int, data[2]))

min_flicks = sum(bool(s != m) for s, m in zip(sherlock_card, moriarty_card))
max_flicks = sum(bool(s != m) for s, m in zip(sherlock_card, moriarty_card))
print(min_flicks)
print(max_flicks)
