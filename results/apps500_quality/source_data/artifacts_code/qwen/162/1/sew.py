def min_hours_to_water_garden(n, k, a):
    # Initialize the minimum hours to a large number
    min_hours = float('inf')
    
    # Iterate over each bucket
    for  bucket in  a:
        # Calculate the number of hours needed to water the garden with the current bucket
        hours=(k+bucket-1)//bucket
        # Update the minimum hours if the current bucket's hours are smaller
        if  hours < min_hours:
            min_hours=hours
    
    # Return the minimum number of hours required to water the garden
    return  min_hours

# Read input from standard input
import  sys
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
k, a = int(data[1]), list(map(int, data[2:]))

# Calculate and print the minimum number of hours required to water the garden
print(min_hours_to_water_garden(n, k, a))
