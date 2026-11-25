# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    h, m = map(int, input().split())
    
    # Calculate the number of minutes before the New Year
    minutes_before_new_year = (23 - h) * 60 + (60 - m - 1)
    
    # Print the result
    print(minutes_before_new_year)
