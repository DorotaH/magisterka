from  collections import  defaultdict

def longest_streak(n, u):
    max_streak = 0
    current_streak = 0
    color_count = defaultdict(int)
    color_frequency = defaultdict(int)

    for i in range(n):
        color = u[i]
        color_count[color] += 1
        color_frequency[color_count[color]] += 1
        color_frequency[color_count[color] - 1] -= 1

        if color_frequency[color_count[color]] == 0:
            del  color_frequency[color_count[color]]

        if len(color_frequency) == 1:
            current_streak = i + 1
        else:
            current_streak = max(current_streak, i)

        max_streak = max(max_streak, current_streak)

    return max_streak


# Read input
n = int(input())
u = list(map(int, input().split()))

# Output the result
print(longest_streak(n, u))
