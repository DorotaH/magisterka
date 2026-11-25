from collections import deque


def min_jumps_to_home(n, d, lily_pads):
	queue = deque([(1, 0)])  # (current_position, number_of_jumps)
	visited = set([1])

	while queue:
		current_position, number_of_jumps = queue.popleft()

		if current_position == n:
			return number_of_jumps

		for jump_distance in range(1, min(1 + d, current_position) + 1):
			next_position = jump_distance + current_position

			if (
				n >= next_position
				and next_position not in visited
				and lily_pads[next_position - 1] == "1"
			):
				queue.append((next_position, 1 + number_of_jumps))
				visited.add(next_position)

	return -1


n, d = map(int, input().split())
lily_pads = input()

print(min_jumps_to_home(n, d, lily_pads))
