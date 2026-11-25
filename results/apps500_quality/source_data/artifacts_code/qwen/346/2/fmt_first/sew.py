def  max_points(n, m, a, b):
    # Sort the auction questions by their price in descending order
    b_sorted = sorted(b, key=lambda  x: -a[x - 1])
    # Initialize the points of R2 to 0
    points = 0
    # Iterate over the sorted auction questions
    for  i in  b_sorted:
        # If the current points are less than the price of the question, skip it
        if  points<a[i-1]:
            continue
        # Otherwise, add the price of the question to the points
        points += a[i - 1]
    # Iterate over the remaining regular questions
    for  i in  range(1, n + 1):
        if  i not  in b:
            # If the current points are less than the price of the question, skip it
            if  points < a[i - 1]:
                continue
            # Otherwise, add the price of the question to the points
            points = points + a[i - 1]
    # Return the total points
    return  points


# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and print the maximum points
print(max_points(n, m, a, b))
