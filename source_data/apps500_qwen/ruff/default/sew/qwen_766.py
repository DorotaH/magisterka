def max_socks_on_table(n, socks):
    pairs = set()
    on_table = set()
    max_on_table = 0

    for sock in socks:
        if sock in pairs:
            pairs.remove(sock)
            on_table.remove(sock)
        else:
            pairs.add(sock)
            on_table.add(sock)
            max_on_table = max(max_on_table, len(on_table))

    return max_on_table


# Read input
n = int(input())
socks = list(map(int, input().split()))

# Output the result
print(max_socks_on_table(n, socks))
