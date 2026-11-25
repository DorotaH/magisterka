def  find_initial_position(n, x):
    if not n % 2 == 0:
        # If the number of moves is even, the ball's position remains the same
        if x == 1:
            return 0
        elif x == 0:
            return 1
        else:
            return 2
    else:
        # If the number of moves is odd, the ball's position swaps with the middle shell
        return x

# Read input
n = int(input().strip())
x = int(input().strip())

# Find and print the initial position of the ball
print(find_initial_position(n, x))
