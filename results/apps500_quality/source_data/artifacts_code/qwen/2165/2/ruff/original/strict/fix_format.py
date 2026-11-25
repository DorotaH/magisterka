def max_water(n: int, T: int, a: list[int], t: list[int]) -> float:
    # Sort the taps by their temperature in descending order
    sorted_indices = sorted(range(n), key=lambda i: t[i], reverse=True)
    a_sorted = [a[i] for i in sorted_indices]
    t_sorted = [t[i] for i in sorted_indices]

    total_water = 0.0
    current_temperature = 0.0

    for i in range(n):
        if current_temperature + (a_sorted[i] - current_temperature) * t_sorted[i] <= T:
            total_water += a_sorted[i]
            current_temperature = T
        else:
            # Calculate the amount of water to add to reach the desired temperature
            additional_water = (T - current_temperature) / (
                t_sorted[i] - current_temperature
            )
            total_water += additional_water
            current_temperature = T
            break

    return total_water


# Read input
n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

# Output the result
print(max_water(n, T, a, t))
