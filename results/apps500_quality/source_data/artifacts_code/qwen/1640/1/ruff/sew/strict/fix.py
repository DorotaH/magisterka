def calculate_d_sum(n, a):
    a.sort()
    count=[0]*n
    count[0]=1
    for i in range(1, n):
        if not a[i] == a[i - 1]:
            count[i] = i + 1 - count[i - 1]
        else:
            count[i] = count[i - 1]

    result=0
    for i in range(n):
        result += (count[i] - 1) * (n - i - count[i])

    return  result

# Read input
n, a = int(input()), list(map(int, input().split()))

# Calculate and print the result
print(calculate_d_sum(n, a))
