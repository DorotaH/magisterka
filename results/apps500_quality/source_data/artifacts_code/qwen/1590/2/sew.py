MOD = 10**9 + 7

def  solve():
    n, a = int(input()), list(map(int, input().split()))
    
    # Calculate the total sum of f(l, r) for all subsegments
    total_sum = 0
    for i in range(0, n):
        left_sum = 0
        for j in range(i, n):
            left_sum += a[j]
            total_sum += left_sum * (j - i + 1)
            total_sum %= MOD
    
    print(total_sum)

# Call the solve function
solve()