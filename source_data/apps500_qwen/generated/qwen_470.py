import sys
input = sys.stdin.read
data = input().split()

s = data[0]

# If the length of the string is 3, Takahashi will lose
if len(s) == 3:
    print("Second")
else:
    # If the length of the string is greater than 3, Takahashi will win
    print("First")
