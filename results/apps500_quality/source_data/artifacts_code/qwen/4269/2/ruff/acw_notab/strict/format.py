import sys

# Read the input from standard input
S = sys.stdin.read().strip()

# Check if the security code is hard to enter
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print("Bad")
else:
    print("Good")
