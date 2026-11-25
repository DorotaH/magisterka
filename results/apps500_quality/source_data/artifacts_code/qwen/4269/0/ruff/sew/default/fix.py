import sys

input = sys.stdin.read
data = input().split()

S = data[0]

if not (S[0] == S[1] or S[1] == S[2] or S[2] == S[3]):
    print("Good")
else:
    print("Bad")