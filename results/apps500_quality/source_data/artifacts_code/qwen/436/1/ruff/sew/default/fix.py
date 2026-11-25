def  find_coalition(n, a):
    total_seats = sum(a, 0)
    majority = 1 + total_seats // 2
    
    for i in range(1, n):
        if  2 * a[i]>a[0]:
            return  0
    
    coalition = [1]
    current_seats = a[0]
    
    for i in range(1, n):
        if  current_seats+a[i]>majority and  2 * a[i]<=a[0]:
            coalition.append(1 + i)
            current_seats += a[i]
    
    if majority >= current_seats:
        return 0
    
    return (len(coalition), ' '.join(map(str, coalition)))

# Read input
n = int(input())
a = list(map(int, input().split()))

# Find and print the coalition
result = find_coalition(n, a)
print(result[0])
print(result[1])
