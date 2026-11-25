def max_occupied_tables(n, k, s):
    free_tables = s.count('0')
    occupied_tables = s.count('1')
    if occupied_tables == 0 or occupied_tables == 1:
        return free_tables

    # Find the maximum number of tables that can be occupied
    max_occupied = 0
    for i in range(n):
        if s[i] == '0':
            # Check if we can place a '1' at this position without violating the rules
            if (i == 0 or s[i-1] == '0') and (i == n-1 or s[i+1] == '0'):
                # Place a '1' and update the string
                new_s = s[:i] + '1' + s[i+1:]
                # Check the number of occupied tables in the new string
                new_occupied = new_s.count('1')
                if new_occupied > max_occupied:
                    max_occupied = new_occupied
                # Remove the '1' to continue checking the next position
                new_s = s[:i] + '0' + s[i+1:]

    return free_tables - (occupied_tables - max_occupied)

# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Process each test case
results = []
index = 0
for t in range(int(data[index])):
    index += 1
    n = int(data[index])
    k = int(data[index + 1])
    s = data[index + 2]
    index += 3
    results.append(max_occupied_tables(n, k, s))

# Print the results
for result in results:
    print(result)
