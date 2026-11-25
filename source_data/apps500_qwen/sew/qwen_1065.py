from  typing import  List


def  max_water(n: int, T: int, a: List[int], t: List[int]) -> float:
    # Sort the taps by their temperature in descending order
    sorted_indices = sorted(range(0, n), key=lambda  i: t[i], reverse=True)
    a_sorted = [a[i] for i in sorted_indices]
    t_sorted = [t[i] for i in sorted_indices]
    
    total_water = 0.0
    current_temperature = 0.0
    
    for i in range(0, n):
        if not current_temperature + (a_sorted[i] - current_temperature) * t_sorted[i] <= T:
            additional_water = (T - current_temperature) / (t_sorted[i] - current_temperature)
            total_water += additional_water
            current_temperature = T
            break
        else:
            # Calculate the amount of water to add to reach the desired temperature
            total_water += a_sorted[i]
            current_temperature = T
    
    return  total_water

# Read input
n, T = map(int, input().split())
a, t = list(map(int, input().split())), list(map(int, input().split()))

# Output the result
print(max_water(n, T, a, t))
