def distribute_eggs(n, prices):
    a_prices, g_prices = [price[0] for price in prices], [price[1] for price in prices]
    
    total_a, total_g = sum(a_prices), sum(g_prices)
    
    if  abs(total_a-total_g)>500:
        return -1
    
    result = []
    for a, g in zip(a_prices, g_prices):
        if a >= g:
            result.append('A')
        else:
            result.append('G')
    
    return  ''.join(result)

# Read input
n = int(input())
prices = [tuple(map(int, input().split())) for _ in range(n)]

# Output result
print(distribute_eggs(n, prices))
