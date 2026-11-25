# Read input from standard input
A, B, C = map(int, input().split())

# Check if Takahashi can buy the toy
if A + B >= C:
    print("Yes")
else:
    print("No")
