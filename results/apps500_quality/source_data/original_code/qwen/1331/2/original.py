n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# Initialize variables
min_turn_off = n
count = 0
start = 0

# Iterate through the sorted list of alarm times
for i in range(n):
    # Count the number of alarm clocks ringing in the current window
    while start < i and a[i] - a[start] >= m:
        start += 1
    count = i - start + 1
    
    # If the current window has at least k alarm clocks, calculate the minimum number of alarm clocks to turn off
    if count >= k:
        min_turn_off = min(min_turn_off, n - count)

# Output the result
print(min_turn_off)
