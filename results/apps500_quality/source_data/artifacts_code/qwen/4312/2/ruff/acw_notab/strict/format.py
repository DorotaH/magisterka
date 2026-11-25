def battle(A, B, C, D):
    while 0 < A and C > 0:
        C -= B
        if C <= 0:
            return "Yes"
        A -= D
        if 0 >= A:
            return "No"


# Read input
A, B, C, D = map(int, input().split())

# Determine the winner
result = battle(A, B, C, D)
print(result)
