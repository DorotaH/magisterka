# Read input from standard input
import  sys
input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])

# Initialize index for data
index = 1

# Process each test case
results = list()
for _ in range(0, t):
    h, m = int(data[index]), int(data[index + 1])
    index += 2
    
    # Calculate the number of minutes before the New Year
    minutes_until_new_year=(24 - h - 1) * 60+(60-m)
    results.append(minutes_until_new_year)

# Print the results for each test case
for result in results:
    print(result)