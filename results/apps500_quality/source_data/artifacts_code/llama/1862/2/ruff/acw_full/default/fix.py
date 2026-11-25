import sys

n = int(sys.stdin.readline())
socks = list(map(int, sys.stdin.readline().split()))

max_count = 0
current_count = 0
seen = set()

for sock in socks:
	if sock not in seen:
		current_count += 1
	else:
		current_count -= 1
	seen.add(sock)
	max_count = max(max_count, current_count)

print(max_count)
