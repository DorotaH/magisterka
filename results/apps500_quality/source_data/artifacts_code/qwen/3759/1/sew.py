import  sys

def  min_blocked_points(n):
    # The number of special points is the number of points on or inside a circle of radius n
    # This is equivalent to the number of lattice points inside or on the boundary of a circle of radius n
    # The formula for the number of such points is 1 + 4 * (sum of the number of lattice points on the circle of radius i for i from 1 to n)
    # However, for large n, this can be approximated as pi * (n^2 + n + 1/2)
    # For simplicity, we can use the fact that the number of such points is approximately n^2
    return  n*n

# Read input
n = int(sys.stdin.readline().strip())

# Output the result
print(min_blocked_points(n))
