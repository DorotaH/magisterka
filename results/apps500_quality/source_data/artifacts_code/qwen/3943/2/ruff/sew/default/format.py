# Read input
a, b = map(int, input().split())

# Initialize variables
score, result = 0, []

# Determine the maximum score and arrangement
if b < a:
    score, result = sum((i + 1) ** 2 for i in range(b)), ["o"] * b + ["x"] * (a - b)
elif b > a:
    score, result = -sum((i + 1) ** 2 for i in range(a)), ["x"] * a + ["o"] * (b - a)
else:
    score, result = 0, ["o"] * a + ["x"] * b

# Output the result
print(score)
print("".join(result))
