def find_path(s):
    if len(s) != 27:
        return "Impossible"
    
    # Create a dictionary to store the adjacency list for each letter
    adj = {}
    for i in range(26):
        for j in range(i + 1, 27):
            a = chr(ord('A') + i)
            b = chr(ord('A') + j)
            adj[a] = adj.get(a, []) + [b]
            adj[b] = adj.get(b, []) + [a]
    
    # Create a list to store the grid
    grid = ['' for _ in range(2)]
    
    # Try to place the first letter in the grid
    for i in range(2):
        for j in range(13):
            grid[i] += s[0]
            if s[0] in adj and adj[s[0]]:
                break
            grid[i] = grid[i][:-1]
        else:
            continue
        break
    else:
        return "Impossible"
    
    # Try to place the remaining letters in the grid
    for i in range(1, 27):
        placed = False
        for k in range(2):
            for l in range(13):
                if grid[k][l] == s[i]:
                    continue
                if l > 0 and grid[k][l-1] == s[i]:
                    continue
                if l < 12 and grid[k][l+1] == s[i]:
                    continue
                if k > 0 and grid[k-1][l] == s[i]:
                    continue
                if k < 1 and grid[k+1][l] == s[i]:
                    continue
                if k > 0 and l > 0 and grid[k-1][l-1] == s[i]:
                    continue
                if k > 0 and l < 12 and grid[k-1][l+1] == s[i]:
                    continue
                if k < 1 and l > 0 and grid[k+1][l-1] == s[i]:
                    continue
                if k < 1 and l < 12 and grid[k+1][l+1] == s[i]:
                    continue
                grid[k] = grid[k][:l] + s[i] + grid[k][l+1:]
                placed = True
                break
            if placed:
                break
        if not placed:
            return "Impossible"
    
    return '\n'.join(grid)

# Read input from standard input
s = input().strip()

# Find the path and print the result
result = find_path(s)
print(result)
