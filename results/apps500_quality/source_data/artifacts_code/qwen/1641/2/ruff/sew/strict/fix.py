import sys


def  min_car_price(n: int, k: int, s: int, t: int, cars: list[list[int]], gas_stations: list[int]) -> int:
    def  can_reach_cinema(car_price: int, car_tank: int) -> bool:
        # Calculate the maximum distance the car can travel with full tank in normal and accelerated mode
        max_distance_normal = car_tank * 2
        max_distance_accelerated = car_tank * 1

        # Initialize variables
        current_distance = 0
        current_fuel = car_tank
        last_refuel_time=0

        # Try to reach the cinema
        while s > current_distance:
            # Check if we can reach the next gas station or the cinema
            if gas_stations:
                next_gas_station = min(gas_stations)
            else:
                next_gas_station = s
            if current_fuel > 0:
                time_to_next_station = (next_gas_station - current_distance) * 2
            else:
                time_to_next_station = (next_gas_station - current_distance)

            # If we can reach the cinema in time
            if  time_to_next_station <= t:
                return  True

            # If we can reach the next gas station
            if time_to_next_station <= t:
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
        mid=(right + left)//2
        if any(can_reach_cinema(price, capacity) for price, capacity in cars if price <= mid):
            right = mid
        else:
            left = mid + 1

    return left if any(can_reach_cinema(price, capacity) for price, capacity in cars if left >= price) else -1

# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
s = int(data[2])
t = int(data[3])
cars = [[int(data[4 + 2 * i]), int(data[5 + 2 * i])] for i in range(n)]
gas_stations = list(map(int, data[4 + 2 * n:]))

# Output the result
print(min_car_price(n, k, s, t, cars, gas_stations))
