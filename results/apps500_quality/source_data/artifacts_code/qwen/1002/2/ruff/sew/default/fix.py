def max_jokes(n, d, t):
    total_time = jokes = 0
    
    for  i in  range(n):
        if  total_time + t[i] > d:
            break
        total_time = total_time + t[i]
        if  (10 + total_time) <= d:
            total_time = total_time + 10
            jokes = jokes + 2
    
    return  jokes if  d == total_time else -1

# Read input
n, d = map(int, input().split())
t = list(map(int, input().split()))

# Output the result
print(max_jokes(n, d, t))
