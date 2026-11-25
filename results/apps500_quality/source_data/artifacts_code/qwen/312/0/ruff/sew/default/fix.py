def optimal_choice(n, m):
    if  m == 1:
        return  2
    elif  n == m:
        return  n-1
    else:
        return  m-1

# Read input
n, m=map(int, input().split())

# Output the result
print(optimal_choice(n, m))