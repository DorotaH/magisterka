def count_magnet_groups(n, magnets):
    groups = 0
    current_group = False
    
    for magnet in magnets:
        if magnet == '10':
            if not current_group:
                groups += 1
                current_group = True
        else:
            current_group = False
    
    return groups

# Read input from standard input
n = int(input().strip())
magnets = []
for _ in range(n):
    magnets.append(input().strip())

# Print the number of groups
print(count_magnet_groups(n, magnets))
