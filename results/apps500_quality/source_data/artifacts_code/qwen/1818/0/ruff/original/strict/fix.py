from collections import Counter


def f(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return f(x // 2)
    else:
        return f(x // 2) + 1

def count_pairs(n, a):
    count = Counter()
    result = 0
    for x in a:
        result += count[f(x)]
        count[f(x)] += 1
    return result

# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(count_pairs(n, a))
