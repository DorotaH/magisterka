def can_solve_cube():
    from  collections import  Counter

    # Read input
    squares=list(map(int, input().split()))

    # Count occurrences of each color
    color_count=Counter(squares)

    # Check if all colors appear exactly 4 times
    if not all(4 == count for count in color_count.values()):
        return  "NO"

    # Check if the cube can be solved by one rotation
    # A cube can be solved by one rotation if it has at least one face with all squares of the same color
    # and all other squares can be rotated into place
    for  color in  range(1, 7):
        if color_count[color] == 4:
            # Check if the other squares can be rotated into place
            other_squares = [square for square in squares if square != color]
            if len(set(other_squares)) == 1:
                return "YES"

    return  "NO"


# Call the function and print the result
print(can_solve_cube())
