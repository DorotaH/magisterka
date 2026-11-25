def  find_x_y(r):
    # Start with x = 1 and increase until we find a valid y or exceed the limit
    x = 1
    while  1:
        # Calculate the left side of the equation x^2 + 2xy + x + 1
        left_side=x**2+x+1
        # If the left side is greater than r, we can't find a valid y
        if  r < left_side:
            return  "NO"
        # Calculate the remaining part to find y
        remaining=r-left_side
        # Check if remaining is divisible by 2x
        if  remaining % (2 * x) == 0:
            y=remaining//(2 * x)
            # If y is a positive integer, we found a valid pair
            if y > 0:
                return f"{x} {y}"
        # Move to the next x
        x = x + 1

# Read input
r=int(input().strip())

# Find and print the result
result=find_x_y(r)
print(result)