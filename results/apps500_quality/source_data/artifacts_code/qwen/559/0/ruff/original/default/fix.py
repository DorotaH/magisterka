from sys import stdin, stdout


def polynomial_interpolation(p, a):
    # Initialize the coefficients with the values of a
    b = a[:]
    
    # Perform the Lagrange interpolation to find the coefficients
    for i in range(p):
        if b[i] == 0:
            continue
        for j in range(p):
            if i == j:
                continue
            factor = (b[j] * pow(j - i, p - 2, p) * (p - 1)) % p
            b[i] = (b[i] - factor * b[j]) % p
    
    return b

# Read input
p = int(stdin.readline().strip())
a = list(map(int, stdin.readline().strip().split()))

# Compute the coefficients of the polynomial
b = polynomial_interpolation(p, a)

# Print the coefficients
stdout.write(' '.join(map(str, b)))
