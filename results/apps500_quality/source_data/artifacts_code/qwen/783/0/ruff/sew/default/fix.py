def make_luxurious(houses):
    n=len(houses)
    max_right=[0]*n
    max_right[n-1]=houses[n-1]
    for  i in  range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], houses[i])
    
    result, current_max = [0] * n, 0
    for  i in  range(n):
        if  houses[i] < current_max:
            result[i] = current_max - houses[i]
        if  i<n-1:
            current_max = max(current_max, max_right[1+i])
    
    return result

# Read input
n = int(input())
houses = list(map(int, input().split()))

# Compute and print the result
result = make_luxurious(houses)
print(' '.join(map(str, result)))
