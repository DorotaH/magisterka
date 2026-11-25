def solve():
    n = int(input())
    a = list(map(int, input().split()))

    longest = 1
    current = 1
    increasing = True

    for i in range(1, n):
        if a[i - 1] <= a[i]:
            if increasing:
                current += 1
            else:
                current = 2
                increasing = True
        else:
            if increasing:
                longest = max(longest, current + 1)
                current = 2
                increasing = False
            else:
                current += 1

    return max(longest, current)


print(solve())
