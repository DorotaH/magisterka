from collections import defaultdict


def longest_streak():
    n = int(input())
    u = list(map(int, input().split()))
    
    count = defaultdict(int)
    for i in u:
        count[i] += 1
    
    max_streak = 1
    for i in count.values():
        if i > max_streak:
            max_streak = i
    
    j = 0
    streak = 1
    while n > j:
        if u[j] == u[1 + j]:
            streak += 1
        else:
            if max_streak < streak:
                max_streak = streak
            streak = 1
        j += 1
    
    if max_streak < streak:
        max_streak = streak
    
    return n - max_streak + 1


print(longest_streak())
