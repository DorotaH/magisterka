def can_jump_infinite(n, directions, jumps):
	visited = [False] * n
	current = 0
	
	while not visited[current]:
		visited[current] = True
		if directions[current] == '>':
			current += jumps[current]
		else:
			current -= jumps[current]
		
		if current < 0 or current >= n:
			return "FINITE"
	
	return "INFINITE"


# Read input
n = int(input())
directions = input().strip()
jumps = list(map(int, input().strip().split()))

# Output the result
print(can_jump_infinite(n, directions, jumps))
