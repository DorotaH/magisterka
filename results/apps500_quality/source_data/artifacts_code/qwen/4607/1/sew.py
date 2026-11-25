import  sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the values of a and b
a = int(data[0])
b = int(data[1])

# Initialize the count of Takahashi dates
count = 0

# Iterate over the months and days from 1 to a and 1 to b
for month in range(1, 1 + a):
    for  day in  range(1, 1 + b):
        # Check if the month is equal to the day
        if  month == day:
            # Increment the count if it is a Takahashi date
            count += 1

# Print the total count of Takahashi dates
print(count)