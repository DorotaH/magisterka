import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse input
n, m = int(data[0]), int(data[1])
k, a = int(data[2]), int(data[3])
b = int(data[4])


# Function to calculate the time to move from apartment a to apartment b
def min_time_to_move(n, m, k, a, b):
    # Calculate the current floor and entrance of apartment a
    entrance_a = (a - 1) // (m * k) + 1
    floor_a = ((a - 1) % (m * k)) // k + 1

    # Calculate the current floor and entrance of apartment b
    entrance_b = (b - 1) // (m * k) + 1
    floor_b = ((b - 1) % (m * k)) // k + 1

    # Calculate the time to move to the same entrance as apartment b
    if entrance_a != entrance_b:
        time_to_same_entrance = 15 + abs(entrance_a - entrance_b) * 15
    else:
        time_to_same_entrance = 0

    # Calculate the time to move from floor a to floor b
    time_to_move_floors = 5 * abs(floor_a - floor_b)

    # Calculate the total time
    total_time = time_to_same_entrance + time_to_move_floors

    return total_time


# Output the result
print(min_time_to_move(n, m, k, a, b))
