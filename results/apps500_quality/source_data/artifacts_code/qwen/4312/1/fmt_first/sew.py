def battle(A, B, C, D):
    while  A > 0 and  C > 0:
        C = C - B
        if C <= 0:
            break
        A = A - D
    return  "No" if  A <= 0 else "Yes"


# Read input
A, B, C, D=map(int, input().split())

# Output the result
print(battle(A, B, C, D))