
def check(car_capacity, time_limit, gas_station_positions):
    """
    Check if it is possible to reach the cinema in time using the given car capacity.

    Args:
        car_capacity (int): The capacity of the car's fuel tank.
        time_limit (int): The time in which the film starts.
        gas_station_positions (list): A list of gas station positions.

    Returns:
        bool: True if it is possible to reach the cinema in time, False otherwise.
    """
    total_distance = 0
    current_time = 0
    for i in range(len(gas_station_positions) - 1):
        distance_to_gas_station = gas_station_positions[i + 1] - gas_station_positions[i]
        # Calculate the time it takes to reach the gas station in accelerated mode
        time_to_gas_station = min(distance_to_gas_station, 2 * distance_to_gas_station)
        # Calculate the time it takes to reach the next gas station in normal mode
        time_to_next_gas_station = 2 * distance_to_gas_station
        # Choose the driving mode that takes less time
        if time_to_gas_station > time_to_next_gas_station:
            time_to_gas_station = time_to_next_gas_station
            distance_to_gas_station = 2 * distance_to_gas_station
        # Update the total distance and current time
        total_distance += distance_to_gas_station
        current_time += time_to_gas_station
    # Calculate the time it takes to reach the cinema from the last gas station
    distance_to_cinema = s - gas_station_positions[-1]
    time_to_cinema = min(distance_to_cinema, 2 * distance_to_cinema)
    # Update the total distance and current time
    total_distance += distance_to_cinema
    current_time += time_to_cinema
    # Check if the car can reach the cinema in time
    return current_time <= time_limit and total_distance <= car_capacity

def binary_search(cars, time_limit, gas_station_positions):
    """
    Find the minimum price of a car that can reach the cinema in time.

    Args:
        cars (list): A list of cars with their prices and capacities.
        time_limit (int): The time in which the film starts.
        gas_station_positions (list): A list of gas station positions.

    Returns:
        int: The minimum price of a car that can reach the cinema in time, or -1 if no such car exists.
    """
    # Initialize the minimum and maximum possible prices
    min_price = 0
    max_price = max(car[0] for car in cars)
    # Perform a binary search to find the minimum price
    while min_price < max_price:
        mid_price = (min_price + max_price) // 2
        # Filter the cars that have a price less than or equal to the mid price
        filtered_cars = [car for car in cars if car[0] <= mid_price]
        # Check if any of the filtered cars can reach the cinema in time
        if any(check(car[1], time_limit, gas_station_positions) for car in filtered_cars):
            # If a car can reach the cinema in time, update the maximum price
            max_price = mid_price
        else:
            # If no car can reach the cinema in time, update the minimum price
            min_price = mid_price + 1
    # Return the minimum price of a car that can reach the cinema in time
    return min_price if any(check(car[1], time_limit, gas_station_positions) for car in cars) else -1

# Read the input
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))
gas_station_positions = sorted(map(int, input().split()))

# Find the minimum price of a car that can reach the cinema in time
min_price = binary_search(cars, t, gas_station_positions)
print(min_price)
