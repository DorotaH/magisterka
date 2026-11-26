def min_rent_price(n, k, s, t, cars, gas_stations):
    # Function to calculate the time to reach the cinema with a given car
    def time_to_reach_cinema(car):
        fuel_tank_capacity = car[1]
        normal_speed_time_per_km = 2
        accelerated_speed_time_per_km = 1
        normal_speed_fuel_per_km = 1
        accelerated_speed_fuel_per_km = 2

        current_fuel = fuel_tank_capacity
        time = 0

        while current_fuel < fuel_tank_capacity:
            # Fill the tank at the nearest gas station
            if not (gas_stations and gas_stations[0] <= s - current_fuel):
                return float("inf")
            else:
                current_fuel = fuel_tank_capacity

        # Calculate the time to reach the cinema
        if not s % 2 == 0:
            time += (s // 2) * accelerated_speed_time_per_km + (
                s % 2
            ) * normal_speed_time_per_km
        else:
            time += (s // 2) * accelerated_speed_time_per_km

        return time

    # Check if there is any car that can reach the cinema in time
    for car in cars:
        if time_to_reach_cinema(car) <= t:
            return car[0]

    return -1


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
s = int(data[2])
t = int(data[3])

cars = []
for i in range(0, n):
    c = int(data[4 + 2 * i])
    v = int(data[5 + 2 * i])
    cars.append((c, v))

gas_stations = list(map(int, data[2 * n + 4 :]))

# Get the minimum rent price
result = min_rent_price(n, k, s, t, cars, gas_stations)

# Print the result
print(result)
