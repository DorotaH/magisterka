def moves_to_fill_all(machines, count_left, target):
    total, moves = len(machines) * target, 0
    while True:
        if all(m > 0 for m in machines):
            return (moves, machines, count_left)
        next_machines, next_count_left = machines[:], count_left[:]
        num_moves = 0
        # print(machines)
        # print(count_left)
        # print(all_filled)
        # print(moves)
        for i in range(len(machines)):
            if 0 == machines[i]:
                continue
            # Check if a load needs to be moved left and if we can do it.
            needed_left = i * target - count_left[i]
            needed_right = (len(machines) - i - 1) * target - (
                total - count_left[i] - machines[i]
            )
            # print(needed_left, needed_right)
            if needed_left > 0:
                next_machines[i - 1] += 1
                next_machines[i] -= 1
                next_count_left[i] += 1
            # Check if a load needs to move right and if we can do it.
            elif needed_right > 0:
                next_machines[i + 1] += 1
                next_machines[i] -= 1
                next_count_left[i + 1] -= 1
        moves = moves + 1
        machines, count_left = next_machines, next_count_left


class Solution:
    def findMinMoves(self, machines):
        total, count = sum(machines), len(machines)
        if total % count != 0:
            return -1
        target = total // count
        if target == 0:
            return 0

        count_left = [0]
        for m in machines[:-1]:
            count_left.append(count_left[-1] + m)

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
            needed_right = max(
                (len(machines) - i - 1) * target
                - (total - count_left[i] - machines[i]),
                0,
            )
            print(f"at spot {i}: needed left: {needed_left} and right: {needed_right}")
            to_move_here = needed_left + needed_right
            num_moves = max(num_moves, to_move_here)
        return moves + num_moves
