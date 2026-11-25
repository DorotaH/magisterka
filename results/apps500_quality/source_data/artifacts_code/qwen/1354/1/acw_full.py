def find_cheating_move(n, k, a, m, shots):
	# Create a list to mark the cells as empty or occupied
	field = [0] * (1 + n)

	# Mark the cells where ships can be placed
	for i in range(n - a + 1):
		field[i] = 1
		for j in range(i + 1, i + a):
			field[j] = 1

	# Check each shot to see if it can be the first move that reveals a ship
	for i in range(m):
		if field[shots[i]] == 1:
			can_be_hit = all(j in shots for j in range(shots[i], a + shots[i]))
			if can_be_hit:
				return i + 1

	# If no such move is found, return -1
	return -1


# Read input from standard input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
a = int(data[2])
m = int(data[3])
shots = list(map(int, data[4:]))

# Find and print the result
result = find_cheating_move(n, k, a, m, shots)
print(result)
