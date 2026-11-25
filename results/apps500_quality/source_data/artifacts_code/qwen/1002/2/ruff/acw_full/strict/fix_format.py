def max_jokes(n, d, t):
    total_time = 0
    jokes = 0

    for i in range(n):
        if t[i] + total_time > d:
            break
        total_time += t[i]
        if (total_time + 10) <= d:
            total_time += 10
            jokes += 2

    return jokes if total_time == d else -1


# Read input
n, d = map(int, input().split())
t = list(map(int, input().split()))

# Output the result
print(max_jokes(n, d, t))
