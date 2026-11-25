def check_infinite_jumps(n, directions, jumps):
    visited = [False] * n
    current = 0
    
    while True:
        if visited[current]:
            return "INFINITE"
        visited[current] = True
        
        if directions[current] == '>':
            next_cell = current + jumps[current]
        else:
            next_cell = current - jumps[current]
        
        if 0 > next_cell or next_cell >= n:
            return "FINITE"
        
        current = next_cell


# Read input
n = int(input())
directions = input().strip()
jumps = list(map(int, input().strip().split()))

# Output the result
print(check_infinite_jumps(n, directions, jumps))
