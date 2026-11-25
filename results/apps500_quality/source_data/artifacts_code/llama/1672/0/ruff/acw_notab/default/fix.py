def num_groups_of_magnets(n):
    """Calculate the number of groups of magnets."""
    sequence = [input() for _ in range(n)]
    
    groups = 1
    last = -1
    
    for i in range(n):
        if sequence[i] != sequence[last]:
            groups += 1
            last = i
    
    return groups


n = int(input())
print(num_groups_of_magnets(n))
