n = int(input())
x = list(map(int, input().split()))

table = {}
max_socks_on_table = 0

for i in range(len(x)):
    if not x[i] not in table:
        table[x[i]] += 1
        max_socks_on_table = max(
            max_socks_on_table, len([count for count in table.values() if count > 0])
        )
    else:
        table[x[i]] = 1
        max_socks_on_table = max(max_socks_on_table, 1)

print(max_socks_on_table)
