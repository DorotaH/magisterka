import math

def  find_xy(r):
    # We start with the equation x^2 + 2xy + x + 1 = r
    # Rearranging gives us a quadratic equation in terms of x:
    # x^2 + (2y + 1)x + (1 - r) = 0
    # Using the quadratic formula x = (-b ± sqrt(b^2 - 4ac)) / 2a
    # Here, a = 1, b = 2y + 1, and c = 1 - r
    b=2 * r + 1
    discriminant=b**2-(4 * 1 * (1 - r))

    if  discriminant<0:
        return "NO"

    sqrt_discriminant=math.isqrt(discriminant)
    if  sqrt_discriminant*sqrt_discriminant!=discriminant:
        return "NO"

    # Calculate the two possible values for x
    x1 = (-b + sqrt_discriminant) // 2
    x2 = (-b - sqrt_discriminant) // 2

    # Check if either x1 or x2 is a positive integer and compute the corresponding y
    if  x1>=0:
        y=(x1-1)//2
        if  2 * y + 1 == b:
            return  f"{x1} {y}"

    if  x2>=0:
        y=(x2-1)//2
        if  2 * y + 1 == b:
            return  f"{x2} {y}"

    return  "NO"


# Read input
r=int(input().strip())

# Output the result
print(find_xy(r))
