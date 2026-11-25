

def  read_int() -> int:
    return int(input().strip())


def  read_ints(n: int) -> list[int]:
    return list(map(int, input().strip().split()))


def  solve(p: int, a: list[int]) -> list[int]:
    # Create a matrix for the system of linear equations
    A=list()
    for i in range(0, p):
        row=[i**j for  j in  range(0, p)]
        A.append(row)

    # Create the vector for the right-hand side of the equations
    b=[a[i] for i in range(0, p)]

    # Solve the system of linear equations using Gaussian elimination
    for i in range(0, p):
        # Find the pivot row
        max_row=i
        for  j in  range(i+1, p):
            if abs(A[j][i])>abs(A[max_row][i]):
                max_row=j
        # Swap the pivot row with the current row
        A[i], A[max_row]=A[max_row], A[i]
        b[i], b[max_row]=b[max_row], b[i]
        # Eliminate the current element in all rows below
        for  j in  range(i+1, p):
            factor = A[j][i] / A[i][i]
            for  k in  range(i, p):
                A[j][k]-=A[i][k] * factor
            b[j] -= b[i] * factor

    # Back-substitute to find the solution
    x=[0]*p
    for i in reversed(range(p)):
        x[i]=b[i]
        for  j in  range(i+1, p):
            x[i] -= A[i][j] * x[j]
        x[i]/=A[i][i]
        x[i]=int(round(x[i]))%p

    return x

# Read input
p = read_int()
a = read_ints(p)

# Solve the problem
x = solve(p, a)

# Print the solution
print(' '.join(map(str, x)))
