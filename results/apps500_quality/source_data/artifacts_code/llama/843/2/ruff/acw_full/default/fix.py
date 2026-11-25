n = int(input())
jump_directions = input()
jump_lengths = list(map(int, input().split()))

current_position = 0
for _ in range(100000):
	if 0 <= current_position < n:
		jump_direction = 1 if jump_directions[current_position] == '>' else -1
		current_position += jump_direction * jump_lengths[current_position]
	else:
		print("FINITE")
		break
else:
	print("INFINITE")
