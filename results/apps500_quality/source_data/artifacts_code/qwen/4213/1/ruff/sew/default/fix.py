N = int(input())
A = list(map(int, input().split()))

# Initialize the minimum and maximum elements to the first element of the array
min_element = A[0]
max_element = A[0]

# Iterate through the array starting from the second element
for i in range(1, N):
    # Update the minimum and maximum elements if the current element is smaller or larger
    min_element = min(min_element, A[i])
    max_element = max(max_element, A[i])

# The maximum absolute difference is the difference between the maximum and minimum elements
print(max_element - min_element)