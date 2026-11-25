def sum_of_tickets(n, a):
    # Initialize variables
    total_tickets=0
    current_start = 1
    current_tickets = 0

    # Iterate through each station
    for i in range(n - 1):
        # If the current station allows tickets to the next station
        if i + 1 <= a[i]:
            current_tickets += 1
        else:
            # Calculate the tickets needed for the current segment
            total_tickets += current_tickets * (n - current_start)
            current_start = i + 1
            current_tickets = 1

    # Add the tickets needed for the last segment
    total_tickets += current_tickets * (n - current_start)

    return total_tickets

# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(sum_of_tickets(n, a))
