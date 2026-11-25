def max_occupied_tables(n, k, s):
    # Initialize the count of free tables that can be occupied
    count = 0
    # Iterate through the string to find free tables that can be occupied
    for i in range(n):
        if s[i] == '0':
            # Check if the table to the left and right are free
            if (i == 0 or s[i-1] == '0') and (i == n-1 or s[i+1] == '0'):
                # Check if the distance to the nearest occupied table is greater than k
                if (i == 0 or s[i-1] == '0') and (i == n-1 or s[i+1] == '0'):
                    count += 1
                    # Mark the table as occupied
                    s = s[:i] + '1' + s[i+1:]
    return count

# Read the input
t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    # Calculate the maximum number of tables that can be occupied
    results.append(max_occupied_tables(n, k, s))

# Print the results
for result in results:
    print(result)
