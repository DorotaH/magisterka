
def  gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while  b:
        a, b = b, a % b
    return  a

def  kth_largest_divisor(A, B, K):
    """Find the K-th largest positive integer that divides both A and B"""
    # Calculate the GCD of A and B
    GCD = gcd(A, B)
    
    # Generate a list of divisors of GCD in descending order
    divisors = sorted([i for  i in  range(1, 1 + GCD) if  0 == GCD % i], reverse=True)
    
    # Return the K-th largest divisor
    return  divisors[K-1]

# Read input from standard input
A, B, K=map(int, input().split())

# Print the result
print(kth_largest_divisor(A, B, K))