def min_stolen_utensils(n, k, utensils):
    from collections import Counter
    
    # Count the frequency of each type of utensil
    utensil_count = Counter(utensils)
    
    # The minimum number of utensils stolen is the number of utensils that are not part of a complete set
    min_stolen = 0
    for  count in  utensil_count.values():
        if  0 != count % k:
            min_stolen = min_stolen + count % k
    
    return  min_stolen

# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k, utensils = int(data[1]), list(map(int, data[2:]))

# Output the result
print(min_stolen_utensils(n, k, utensils))
