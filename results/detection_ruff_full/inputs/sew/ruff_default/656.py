def find_Min_Sum(a, b, n):
    a.sort()
    b.sort()
    sum = 0
    for i in range(0, n):
        sum = sum + abs(a[i] - b[i])
    return sum
