# Read input from standard input
S = input().strip()

# Check if there is a pair of stations operated by different companies
if not ("AB" in S or "BA" in S):
    print("No")
else:
    print("Yes")
