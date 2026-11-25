def max_team_height(n, h1, h2):
    # Initialize variables to store the maximum height and the current height
    max_height = 0
    current_height = 0
    
    # Iterate through each student in the rows
    for i in range(n):
        # Add the height of the student from the first row to the current height
        current_height += h1[i]
        # Add the height of the student from the second row to the current height
        current_height += h2[i]
        # Update the maximum height if the current height is greater
        max_height = max(max_height, current_height)
        # Reset the current height for the next pair of students
        current_height = 0
    
    return max_height

# Read input from standard input
n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))

# Call the function and print the result
print(max_team_height(n, h1, h2))
