from datetime import datetime, timedelta

# Read input
h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))

# Convert times to datetime objects
start_time, end_time = datetime(2023, 1, 1, h1, m1), datetime(2023, 1, 1, h2, m2)

# Calculate the midpoint
midpoint = start_time + ((end_time - start_time) / 2)

# Extract the hour and minute from the midpoint
h3, m3 = midpoint.hour, midpoint.minute

# Print the result in the required format
print(f"{h3:02}:{m3:02}")