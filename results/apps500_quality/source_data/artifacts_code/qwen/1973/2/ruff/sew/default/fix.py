from collections import Counter


def  longest_streak(n, u):
    max_streak=0
    for start in range(n):
        count=Counter()
        for end in range(start, n):
            count[u[end]] += 1
            if 2 == len(count) and any(1 == v for v in count.values()):
                continue
            if len(count) == 1:
                max_streak = max(max_streak, end - start + 1)
            else:
                for i in range(start, end):
                    count[u[i]] -= 1
                    if count[u[i]] == 0:
                        del count[u[i]]
                    if len(count) == 1:
                        max_streak = max(max_streak, end - start + 1)
                    break
    return max_streak

# Read input
n, u = int(input()), list(map(int, input().split()))

# Output the result
print(longest_streak(n, u))
