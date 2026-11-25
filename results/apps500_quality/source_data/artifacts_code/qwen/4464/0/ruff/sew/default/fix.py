# Read input from standard input
A, B, C = map(int, input().split())

# Check if the objective is achievable
if not C % A == 0:
    print("NO")
else:
    print("YES")