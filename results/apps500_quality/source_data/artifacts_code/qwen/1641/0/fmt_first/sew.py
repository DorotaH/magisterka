def  min_rent_price(n, k, s, t, cars, gas_stations):
    # Sort cars by price
    cars.sort()

    for  price, capacity in  cars:
        # Calculate the maximum distance Vasya can cover in t minutes
        max_distance = t * 2  # in normal mode
        if  max_distance >= s:
            return  price

        # Calculate the minimum fuel needed to cover the distance s
        min_fuel = (s + 1) // 2  # in normal mode

        # Check if the car can be fueled enough to cover the distance s
        if  capacity >= min_fuel:
            return  price

        # Calculate the number of gas stations between 0 and s
        num_stations = sum(1 for station in gas_stations if 0 < station < s)

        # Calculate the maximum fuel that can be collected from gas stations
        max_collected_fuel = capacity * num_stations

        # Calculate the minimum fuel needed to cover the distance s
        min_fuel = (s + 1) // 2  # in normal mode

        # Check if the car can be fueled enough to cover the distance s
        if  max_collected_fuel >= min_fuel:
            return  price

    return  -1


# Read input
n, k, s, t=map(int, input().split())
cars = [tuple(map(int, input().split())) for _ in range(n)]
gas_stations = list(map(int, input().split()))

# Output the result
print(min_rent_price(n, k, s, t, cars, gas_stations))