import sys

input = sys.stdin.readline

n, k = map(int, input().split())
beauty = list(map(int, input().split()))
colors = input().strip()

max_beauty = 0

# Split colors into lists
white = [beauty[i] for i in range(n) if colors[i] == 'W']
orange = [beauty[i] for i in range(n) if colors[i] == 'O']
red = [beauty[i] for i in range(n) if colors[i] == 'R']

# Sort each list in descending order
white.sort(reverse=True)
orange.sort(reverse=True)
red.sort(reverse=True)

if k == n:
	print(-1)
elif k == 1:
	print(0)
else:
	if len(white) >= 2 and orange:
		max_beauty = max(max_beauty, white[1] + white[0] + orange[0])
	if len(orange) >= 2:
		max_beauty = max(max_beauty, orange[1] + orange[0])
	if len(red) >= 2:
		max_beauty = max(max_beauty, red[1] + red[0])
	if len(orange) >= 2 and red:
		max_beauty = max(max_beauty, orange[1] + orange[0] + red[0])
	if white and orange and red:
		max_beauty = max(max_beauty, white[0] + orange[0] + red[0])
	print(max_beauty)
