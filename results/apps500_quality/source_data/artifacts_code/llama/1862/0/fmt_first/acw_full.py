n = int(input())
socks = list(map(int, input().split()))

max_table_socks = 0
current_table_socks = 0
socks_on_table = set()

for sock in socks:
	if sock in socks_on_table:
		socks_on_table.remove(sock)
	else:
		socks_on_table.add(sock)
		current_table_socks += 1
	max_table_socks = max(max_table_socks, current_table_socks)

print(max_table_socks)
