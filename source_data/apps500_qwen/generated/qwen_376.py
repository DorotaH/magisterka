def max_jokes(n, d, times):
    total_time = 0
    jokes = 0
    
    for i in range(n):
        if total_time + times[i] + 10 > d:
            break
        total_time += times[i] + 10
        jokes += 5
    
    if total_time < times[-1]:
        return -1
    
    return jokes

# Read input
n, d = map(int, input().split())
times = list(map(int, input().split()))

# Output the result
print(max_jokes(n, d, times))
