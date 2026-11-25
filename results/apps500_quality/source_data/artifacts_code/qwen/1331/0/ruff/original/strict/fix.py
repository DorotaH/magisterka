def min_alarm_clocks_to_turn_off(n, m, k, alarms):
    # Sort the alarms by their ringing time
    alarms.sort()

    # Initialize variables
    turn_off_count = 0
    i = 0

    while i < n:
        # Find the end of the current segment of consecutive ringing alarm clocks
        end = i + 1
        while end < n and alarms[end] - alarms[i] < m:
            end += 1

        # If the number of alarm clocks in the segment is less than k, we don't need to turn any off
        if end - i < k:
            i = end
        else:
            # Otherwise, turn off all alarm clocks in the segment except for the last one
            turn_off_count += end - i - 1
            i = end

    return turn_off_count

# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])
alarms = list(map(int, data[3:]))

# Output the result
print(min_alarm_clocks_to_turn_off(n, m, k, alarms))
