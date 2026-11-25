def magic_buns(n, heights):
    # Sort the list of heights in ascending order
    heights.sort()

    # Calculate the median of the heights
    median = (
        heights[len(heights) // 2]
        if len(heights) % 2 != 0
        else (heights[len(heights) // 2 - 1] + heights[len(heights) // 2]) / 2
    )

    # Initialize the step of the progression
    step = 0

    # Initialize the minimum and maximum possible values for the step
    min_step = 0
    max_step = max(heights) - min(heights)

    # Binary search to find the minimum step
    while min_step <= max_step:
        mid_step = (max_step + min_step) // 2

        # Calculate the new heights array with the current step
        new_heights = [h + mid_step * (i - 1) for i in range(1, n + 1)]

        # Check if the new heights array is non-decreasing
        if not all(new_heights[i] <= new_heights[i + 1] for i in range(n - 1)):
            # Update the minimum step
            min_step = mid_step + 1
        else:
            # Update the minimum step
            max_step = mid_step - 1

    # Calculate the maximum number of buns eaten by a student
    max_buns = max(abs(h - median) for h in heights)

    # Calculate the height of the lowest student in the end
    lowest_student_height = min(heights) + min_step

    return max_buns, lowest_student_height, min_step


# Read the input from standard input
n = int(input())
heights = list(map(int, input().split()))

# Calculate and print the result
max_buns, lowest_student_height, step = magic_buns(n, heights)
print(max_buns)
print(lowest_student_height, step)
