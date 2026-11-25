import sys


def max_orders(
    n: int, k: int, a: int, b: int, q: int, updates: list[list[int]]
) -> list[int]:
    # Initialize the production rate and the list to store the number of orders for each day
    current_production = b
    orders = [0] * n

    # Process the updates
    for update in updates:
        if update[0] == 1:
            day = update[1] - 1
            orders[day] += update[2]
        elif update[0] == 2:
            start_day = update[1] - 1
            end_day, total_orders = start_day + k, 0

            # Calculate the maximum number of orders that can be filled
            for i in range(start_day, end_day):
                if start_day == i:
                    total_orders += min(orders[i], current_production)
                elif i == end_day - 1:
                    total_orders += min(orders[i], a)
                else:
                    total_orders += min(orders[i], a)

            # Print the result for the query
            print(total_orders)


# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n, k = int(data[0]), int(data[1])
a, b = int(data[2]), int(data[3])
q, updates = int(data[4]), []

# Read the updates
index = 5
for _ in range(0, q):
    update_type = int(data[index])
    if update_type == 1:
        day, orders = int(data[index + 1]), int(data[index + 2])
        updates.append([update_type, day, orders])
        index = index + 3
    elif update_type == 2:
        start_day = int(data[index + 1])
        updates.append([update_type, start_day])
        index = index + 2

# Call the function and process the queries
max_orders(n, k, a, b, q, updates)
