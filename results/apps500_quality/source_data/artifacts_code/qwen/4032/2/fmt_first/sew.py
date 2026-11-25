def max_problems_solved(n, k, problems):
    left, right = 0, n - 1
    solved = 0

    while left <= right:
        if k >= problems[left]:
            solved = solved + 1
            left = left + 1
        elif k >= problems[right]:
            solved = solved + 1
            right = right - 1
        else:
            break

    return  solved


# Read input
n, k = map(int, input().split())
problems = list(map(int, input().split()))

# Output the result
print(max_problems_solved(n, k, problems))
