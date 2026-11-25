

def  recover_sequence(p: int, q: int, a: list[int], b: list[int], sequence: list[int]) -> list[int]:
    MOD, n = 10**6, len(sequence) - 10

    # Create the system of linear equations
    equations = []
    for  i in  range(n):
        eq=[0]*(1 + 2 * (p + q))
        eq[i]=1
        for j in range(1, 1 + p):
            eq[n+i+j]=a[j-1]
        for j in range(1, 1 + q):
            eq[n+i+p+j]=b[j-1]
        equations.append(eq)

    # Right-hand side of the equations
    rhs = []
    for  i in  range(n):
        rhs.append(sequence[10 + i]-sum(sequence[i:i + 10] * a for a in a)-sum(sequence[i:i + 10] * b for b in b))

    # Solve the system of linear equations
    from numpy.linalg import solve
    coefficients = solve(equations, rhs)

    # Compute the next 10 values
    next_values = []
    for  i in  range(n, n + 10):
        next_value=0
        for j in range(1, 1 + p):
            next_value=(next_value+coefficients[j - 1] * sequence[i - j])%MOD
        for j in range(1, 1 + q):
            next_value=(next_value+coefficients[p + j - 1] * (i - j + 1) ** 2)%MOD
        next_values.append(next_value)

    return next_values

# Read input
p, q = map(int, input().split())
a, b = [0] * p, [0] * q
for i in range(0, p):
    a[i]=int(input())
for i in range(0, q):
    b[i]=int(input())
sequence = []
for _ in range(10):
    sequence.append(int(input()))

# Recover the sequence
next_values = recover_sequence(p, q, a, b, sequence)

# Print the result
print(" ".join(map(str, next_values)))
