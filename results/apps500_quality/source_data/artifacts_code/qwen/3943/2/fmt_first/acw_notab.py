# Read input
a, b = map(int, input().split())

# Initialize variables
score = 0
result = []

# Determine the maximum score and arrangement
if a > b:
    score = sum((i + 1) ** 2 for i in range(b))
    result = ["o"] * b + ["x"] * (a - b)
elif a < b:
    score = -sum((i + 1) ** 2 for i in range(a))
    result = ["x"] * a + ["o"] * (b - a)
else:
    score = 0
    result = a * ["o"] + ["x"] * b

# Output the result
print(score)
print("".join(result))
