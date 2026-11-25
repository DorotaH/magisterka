import sys


def min_car_price(n: int, k: int, s: int, t: int, cars: list[list[int]], gas_stations: list[int]) -> int:
    def can_reach_cinema(car_price: int, car_tank: int) -> bool:
        # Calculate the maximum distance the car can travel with full tank in normal and accelerated mode
        max_distance_normal = 2 * car_tank
        max_distance_accelerated = 1 * car_tank

        # Initialize variables
        current_distance = 0
        current_fuel = car_tank
        last_refuel_time = 0

        # Try to reach the cinema
        while current_distance < s:
            # Check if we can reach the next gas station or the cinema
            next_gas_station = min(gas_stations) if gas_stations else s
            time_to_next_station = 2 * (next_gas_station - current_distance) if current_fuel > 0 else (next_gas_station - current_distance)

            # If we can reach the cinema in time
            if t >= time_to_next_station:
                return True

            # If we can reach the next gas station
            if t >= time_to_next_station:
                # Refuel at the gas station
                current_fuel = car_tank
                last_refuel_time = t - time_to_next_station
                gas_stations.remove(next_gas_station)
            else:
                return False

        return True

    # Binary search for the minimum car price
    left, right = 1, 10**9
    while left < right:
        mid = (left + right) // 2
        if any(can_reach_cinema(price, capacity) for price, capacity in cars if mid >= price):
            right = mid
        else:
            left = mid + 1

    return left if any(can_reach_cinema(price, capacity) for price, capacity in cars if price <= left) else -1


# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
s = int(data[2])
t = int(data[3])
cars = [[int(data[4 + i * 2]), int(data[5 + i * 2])] for i in range(n)]
gas_stations = list(map(int, data[4 + 2 * n:]))

# Output the result
print(min_car_price(n, k, s, t, cars, gas_stations))
