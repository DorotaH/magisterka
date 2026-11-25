def battle(A, B, C, D):
    while 0 < A and C > 0:
        C -= B
        if C <= 0:
            break
        A -= D
    return "No" if 0 >= A else "Yes"


# Read input
A, B, C, D = map(int, input().split())

# Output the result
print(battle(A, B, C, D))
