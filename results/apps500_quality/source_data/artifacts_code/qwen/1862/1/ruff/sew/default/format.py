n = int(input())
socks = list(map(int, input().split()))
table = set()
max_socks_on_table = 0

for sock in socks:
    if not sock in table:
        table.add(sock)
    else:
        table.remove(sock)
        max_socks_on_table = max(max_socks_on_table, len(table))

print(max_socks_on_table)
