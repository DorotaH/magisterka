import sys


def min_time_to_reach(n, m, k, a, b):
    # Calculate the total number of apartments
    total_apartments = n * m * k

    # Calculate the current and target apartment positions
    current_apartment = a - 1
    target_apartment = b - 1

    # Calculate the number of apartments between the current and target positions
    apartments_between = (target_apartment - current_apartment) % (n * m * k)

    # Calculate the number of apartments between the current and target positions in the opposite direction
    apartments_between_opposite = (n * m * k - apartments_between) % (n * m * k)

    # Calculate the time to reach the target apartment using the elevator
    elevator_time = min(apartments_between, apartments_between_opposite) * 10 + 1

    # Calculate the time to reach the target apartment using the stairs
    stairs_time = min(apartments_between, apartments_between_opposite) * 5

    # Return the minimum time
    return min(elevator_time, stairs_time)

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
m = int(data[1])
k = int(data[2])
a = int(data[3])
b = int(data[4])

# Calculate the minimum time to reach the target apartment
result = min_time_to_reach(n, m, k, a, b)

# Print the result
print(result)
