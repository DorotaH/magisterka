from typing import List


def recover_sequence(
    p: int, q: int, a: List[int], b: List[int], sequence: List[int]
) -> List[int]:
    MOD = 10**6
    n = len(sequence) - 10

    # Create the system of linear equations
    equations = []
    for i in range(n):
        eq = [0] * (2 * (p + q) + 1)
        eq[i] = 1
        for j in range(1, p + 1):
            eq[i + n + j] = a[j - 1]
        for j in range(1, q + 1):
            eq[i + n + p + j] = b[j - 1]
        equations.append(eq)

    # Right-hand side of the equations
    rhs = []
    for i in range(n):
        rhs.append(
            sequence[i + 10]
            - sum(sequence[i : i + 10] * a for a in a)
            - sum(sequence[i : i + 10] * b for b in b)
        )

    # Solve the system of linear equations
    from numpy.linalg import solve

    coefficients = solve(equations, rhs)

    # Compute the next 10 values
    next_values = []
    for i in range(n, n + 10):
        next_value = 0
        for j in range(1, p + 1):
            next_value = (next_value + coefficients[j - 1] * sequence[i - j]) % MOD
        for j in range(1, q + 1):
            next_value = (next_value + coefficients[p + j - 1] * (i - j + 1) ** 2) % MOD
        next_values.append(next_value)

    return next_values


# Read input
p, q = map(int, input().split())
a = [0] * p
b = [0] * q
for i in range(p):
    a[i] = int(input())
for i in range(q):
    b[i] = int(input())
sequence = [int(input()) for _ in range(10)]

# Recover the sequence
next_values = recover_sequence(p, q, a, b, sequence)

# Print the result
print(" ".join(map(str, next_values)))
