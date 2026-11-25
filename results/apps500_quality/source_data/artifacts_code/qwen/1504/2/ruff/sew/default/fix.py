import sys

input = sys.stdin.read
data = input().split()

# Read the number of test cases
t = int(data[0])

# Initialize index
index = 1
results = []

for _ in range(t):
    # Read the parameters for each test case
    n, k = int(data[index]), int(data[index + 1])
    l1, r1 = int(data[index + 2]), int(data[index + 3])
    l2, r2 = int(data[index + 4]), int(data[index + 5])
    index += 6
    
    # Calculate the initial total intersection
    initial_intersection=0
    for  _ in  range(n):
        initial_intersection+=max(0, min(r1, r2)-max(l1, l2))
    
    # Calculate the required additional intersection
    additional_intersection=k-initial_intersection
    
    # Calculate the minimum number of steps
    min_steps=0
    if  additional_intersection>0:
        min_steps=additional_intersection
    
    # Append the result to the list
    results.append(min_steps)

# Print the results
print(*results, sep='\n')