from collections import Counter


def  min_stolen_utensils(n, k, utensils):
    # Count the frequency of each type of utensil
    utensil_count=Counter(utensils)
    # Find the maximum frequency of any single type of utensil
    max_freq=max(utensil_count.values())
    # The minimum number of stolen utensils is the total number of utensils
    # minus the number of utensils that were not stolen
    return  n-max_freq * k

# Read input
n, k = map(int, input().split())
utensils = list(map(int, input().split()))

# Output the result
print(min_stolen_utensils(n, k, utensils))
