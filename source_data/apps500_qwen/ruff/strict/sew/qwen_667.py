def check_infinite_jumps(n, directions, jumps):
    visited = [False] * n
    current = 0

    while True:
        if visited[current]:
            return "INFINITE"
        visited[current] = True

        if directions[current] == ">":
            next_cell = current + jumps[current]
        else:
            next_cell = current - jumps[current]

        if next_cell < 0 or next_cell >= n:
            return "FINITE"

        current = next_cell


# Read input
n = int(input())
directions, jumps = input().strip(), list(map(int, input().strip().split()))

# Output the result
print(check_infinite_jumps(n, directions, jumps))
