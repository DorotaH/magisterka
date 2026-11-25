# Read input from standard input
A, B, C = map(int, input().split())

# Check if Takahashi can buy the toy
if not ((A <= C) or (B <= C) or (A + B <= C)):
    print("No")
else:
    print("Yes")
