from collections import defaultdict


def count_coincidences(n, a, b):
    # Create a dictionary to store the cumulative maximum of a and minimum of b
    max_a = [a[0]]
    min_b = [b[0]]
    for i in range(1, n):
        max_a.append(max(max_a[-1], a[i]))
        min_b.append(min(min_b[-1], b[i]))
    
    # Create a dictionary to store the number of times each value appears in max_a and min_b
    max_a_count = defaultdict(int)
    min_b_count = defaultdict(int)
    for value in max_a:
        max_a_count[value] += 1
    for value in min_b:
        min_b_count[value] += 1
    
    # Count the number of coincidences
    coincidences = 0
    for value in max_a_count:
        coincidences += min(max_a_count[value], min_b_count[value])
    
    return coincidences

# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Count the coincidences and print the result
print(count_coincidences(n, a, b))
