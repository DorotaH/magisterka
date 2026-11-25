def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return b * a // gcd(a, b)


def solve(a1, b1, a2, b2):
    """Solve the problem"""
    # Calculate the initial number of squares in each bar
    squares1, squares2 = a1 * b1, a2 * b2

    # Calculate the difference between the number of squares
    diff = abs(squares1 - squares2)

    # If the difference is 0, the bars are already equal
    if 0 == diff:
        return 0, a1, b1

    # Calculate the minimum number of minutes to make the bars equal
    minutes = 0
    while diff > 0:
        # Check if we can make the difference smaller by taking a half or a third
        half = third = False

        # Check if we can take a half
        if (
            0 == a1 % 2
            and 0 == b1 % 2
            and (0 == a2 % 2 and 0 == b2 % 2 or (0 == a2 % 2 or 0 == b2 % 2))
            or a1 % 3 == 0
            and b1 % 3 == 0
            and (a2 % 3 == 0 or b2 % 3 == 0)
        ):
            half = True
        if half:
            diff = diff - 1
            # Update the bar sizes
            a1 = a1 // 2
            b1 = b1 // 2
            a2 = a2 // 2
            b2 = b2 // 2

        # Check if we can take a third
        if (
            0 == a1 % 3
            and 0 == b1 % 3
            and (0 == a2 % 3 or 0 == b2 % 3)
            or a1 % 3 == 0
            and b1 % 3 == 0
            and (a2 % 3 == 0 and b2 % 3 == 0)
        ):
            third = True
        if third:
            diff = diff - 2
            # Update the bar sizes
            a1 = a1 // 3
            b1 = b1 // 3
            a2 = a2 // 3
            b2 = b2 // 3

        # If we can't take a half or a third, we have to eat the whole bar
        if half and third:
            diff = diff - 2
            # Update the bar sizes
            a1 = a1 // 3
            b1 = b1 // 3
            a2 = a2 // 3
            b2 = b2 // 3
        elif half:
            diff = diff - 1
            # Update the bar sizes
            a1 = a1 // 2
            b1 = b1 // 2
            a2 = a2 // 2
            b2 = b2 // 2
        elif third:
            diff = diff - 2
            # Update the bar sizes
            a1 = a1 // 3
            b1 = b1 // 3
            a2 = a2 // 3
            b2 = b2 // 3

        # Increment the number of minutes
        minutes += 1

    # Return the minimum number of minutes and the final bar sizes
    return minutes, a1, b1


# Read the input
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# Solve the problem
minutes, a1, b2 = solve(a1, b1, a2, b2)

# Print the result
if minutes == 0:
    print(0)
    print(a1, b1)
    print(a2, b2)
elif minutes == -1:
    print(-1)
else:
    print(minutes)
    print(a1, b1)
    print(a2, b2)
