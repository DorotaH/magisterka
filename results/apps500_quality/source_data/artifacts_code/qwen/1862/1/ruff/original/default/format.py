n = int(input())
socks = list(map(int, input().split()))
table = set()
max_socks_on_table = 0

for sock in socks:
    if sock in table:
        table.remove(sock)
        max_socks_on_table = max(max_socks_on_table, len(table))
    else:
        table.add(sock)

print(max_socks_on_table)
