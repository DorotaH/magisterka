def check_jump_area(n, directions, lengths):
    visited = set()
    current = 0
    while current not in visited:
        visited.add(current)
        if current < 0 or current >= n:
            return "FINITE"
        direction = directions[current]
        length = lengths[current]
        if direction == '<':
            current -= length
        else:
            current += length
    return "INFINITE"


# Read input
n = int(input())
directions = input().strip()
lengths = list(map(int, input().strip().split()))

# Check the jump area and print the result
result = check_jump_area(n, directions, lengths)
print(result)
