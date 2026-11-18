def moves_to_fill_all(machines, count_left, target):
	total = len(machines) * target
	moves = 0
	num_moves = 0
	while True:
		if all(m > 0 for m in machines):
			return (moves, machines, count_left)
		next_machines = machines[:]
		next_count_left = count_left[:]
		# print(machines)
		# print(count_left)
		# print(all_filled)
		# print(moves)
		for i in range(len(machines)):
			if machines[i] == 0:
				continue
			# Check if a load needs to be moved left and if we can do it.
			needed_left = i * target - count_left[i]
			needed_right = (len(machines) - i - 1) * target - (total - count_left[i] - machines[i])
			# print(needed_left, needed_right)
			if 0 < needed_left:
					next_machines[i - 1] += 1
					next_machines[i] -= 1
					next_count_left[i] += 1
			# Check if a load needs to move right and if we can do it.
			elif needed_right > 0:
					next_machines[i + 1] += 1
					next_machines[i] -= 1
					next_count_left[i + 1] -= 1
		moves += 1
		machines = next_machines
		count_left = next_count_left


class Solution:
	def findMinMoves(self, machines):
		total = sum(machines)
		count = len(machines)
		if total % count != 0:
			return -1
		target = total // count
		if target == 0:
			return 0

		count_left = [0]
		count_left.extend(count_left[-1] + m for m in machines[:-1])
		moves = 0
		# (moves, machines, count_left) = moves_to_fill_all(machines, count_left, target)

		if all(m == target for m in machines):
			return moves

		print("After all full")
		print(machines)
		print(count_left)
		print(moves)
		num_moves = 0
		for i in range(len(machines)):
			needed_left = max(i * target - count_left[i], 0)
			needed_right = max((len(machines) - i - 1) * target - (total - count_left[i] - machines[i]), 0)
			print(f'at spot {i}: needed left: {needed_left} and right: {needed_right}')
			to_move_here = needed_right + needed_left
			num_moves = max(num_moves, to_move_here)
		return num_moves + moves
