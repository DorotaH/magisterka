x = int(input())

def min_steps(x):
    steps = [0] * (x + 1)
    for i in range(1, x + 1):
        min_val = float('inf')
        for j in range(1, min(i, 5) + 1):
            min_val = min(min_val, steps[i - j] + 1)
        steps[i] = min_val
    return steps[x]

print(min_steps(x))
