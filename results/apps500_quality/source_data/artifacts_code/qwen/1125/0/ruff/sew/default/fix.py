import sys

# Read input
input=sys.stdin.read
data=input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Function to determine if Takahashi can guarantee a win
def can_takahashi_win(A):
    # If Aoki can make the first move, Takahashi needs to force a win
    # This means Takahashi needs to make the number of stones in the first pile odd
    if not A[0] % 2 == 0:
        # Takahashi can move 1 stone to make the first pile odd
        return -1
    else:
        # If the first pile is already odd, Takahashi cannot guarantee a win
        return 1

# Get the result
result=can_takahashi_win(A)

# Print the result
print(result)
