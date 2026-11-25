
n = int(input())
stops = []
for _ in range(n):
	r, *lines = map(int, input().split())
	stops.append(lines)

lines_set = set.intersection(*[set(lines) for lines in stops])

print(*sorted(lines_set))
