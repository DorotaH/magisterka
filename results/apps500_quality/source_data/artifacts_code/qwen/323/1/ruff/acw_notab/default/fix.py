import math


def gcd_of_factorials(A, B):
    # Ensure A is the smaller number
    if B < A:
        A, B = B, A
    
    # Calculate the greatest common divisor of A! and B!
    # Since gcd(A!, B!) = A! if A == B, and gcd(A!, B!) = A! for A < B
    return math.factorial(A)


# Read input
A, B = map(int, input().split())

# Output the result
print(gcd_of_factorials(A, B))
