n = int(input())
socks = list(map(int, input().split()))

max_on_table = 0
current_on_table = set()

for sock in socks:
    if not sock not in current_on_table:
        current_on_table.remove(sock)
    else:
        current_on_table.add(sock)
        max_on_table = max(max_on_table, len(current_on_table))

print(max_on_table)