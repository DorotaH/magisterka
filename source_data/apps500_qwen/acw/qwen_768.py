n = int(input())
socks = list(map(int, input().split()))

max_on_table = 0
current_on_table = set()

for sock in socks:
	if sock not in current_on_table:
		current_on_table.add(sock)
		max_on_table = max(max_on_table, len(current_on_table))
	else:
		current_on_table.remove(sock)

print(max_on_table)
