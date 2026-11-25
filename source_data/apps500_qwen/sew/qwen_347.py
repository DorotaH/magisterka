def min_time_to_collect_prizes(n, positions):
    total_time = 0
    friend_position = 10**6
    
    for position in positions:
        # Calculate the time for the friend to move to the position
        friend_time = abs(friend_position - position)
        # Calculate the time for you to move to the position
        your_time = abs(1 - position)
        
        # The friend will pick the prize if it takes less time for the friend
        if friend_time < your_time:
            total_time += friend_time
            friend_position = position
        else:
            total_time += your_time
            friend_position = 1
    
    return total_time

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
positions = list(map(int, data[1:]))

# Calculate and print the result
print(min_time_to_collect_prizes(n, positions))
