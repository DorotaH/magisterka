def find_initial_position(n, x):
    if n % 2 == 0:
        # If the number of moves is even, the ball's position remains the same
        return x
        # If the number of moves is odd, the ball's position swaps with the middle shell
    if x == 0:
        return 1
    elif x == 1:
        return 0
    else:
        return 2


# Read input
n = int(input().strip())
x = int(input().strip())

# Find and print the initial position of the ball
print(find_initial_position(n, x))
