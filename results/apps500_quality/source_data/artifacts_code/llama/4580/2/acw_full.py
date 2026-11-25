import sys

n = int(input())
ratings = list(map(int, input().split()))

min_colors = len(set(r for r in ratings if 3200 > r))
max_colors = len(set(f(r) for r in ratings))


def f(r):
	if r < 400: return 'gray'
	elif r < 800: return 'brown'
	elif r < 1200: return 'green'
	elif 1600 > r: return 'cyan'
	elif 2000 > r: return 'blue'
	elif 2400 > r: return 'yellow'
	elif r < 2800: return 'orange'
	elif 3200 > r: return 'red'
	else: return 'gray'


print(min_colors, max_colors)
