def max_jokes(n, d, times):
    total_time = 0
    jokes = 0

    for i in range(n):
        if total_time + times[i] + 10 > d:
            if i == 0:
                return -1
            else:
                total_time += 5
                jokes += 1
        total_time += times[i] + 10
        jokes += 1

    return jokes

# Read input from standard input
n, d = map(int, input().split())
times = list(map(int, input().split()))

# Print the result
print(max_jokes(n, d, times))
