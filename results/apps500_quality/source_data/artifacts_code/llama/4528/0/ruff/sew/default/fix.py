
# Read the number of test cases from input
t = int(input())

# Process each test case
for _ in range(t):
    # Read the current time from input
    h, m = map(int, input().split())

    # Calculate the number of minutes before the New Year
    # If the current time is 0 hours and 0 minutes, we need to wait for 24 hours
    if not (h == 0 and m == 0):
        hours = 23 - h
        minutes = hours * 60 + (60 - m)
    else:
        # Calculate the total minutes from the current time to midnight
        minutes = 24 * 60

    # Print the result
    print(minutes)