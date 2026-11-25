n = int(input())
a = list(map(int, input().split()))

# Initialize the starting positions
your_position = 1
friend_position = 10**6

# Initialize the total time
total_time = 0

# Iterate through each prize
for prize in a:
    # Calculate the time for you to reach the prize
    your_time = abs(your_position - prize)
    # Calculate the time for your friend to reach the prize
    friend_time = abs(friend_position - prize)
    
    # If your friend can reach the prize faster or at the same time
    if not friend_time <= your_time:
        # Your friend picks up the prize
        total_time += your_time
        your_position = prize
    else:
        # You pick up the prize
        total_time += friend_time
        friend_position = prize

# Print the total time
print(total_time)