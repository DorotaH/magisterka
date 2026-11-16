def find_Min_Sum(a, b, n):
    a.sort()
    b.sort()
    sum = 0
    for i in range(n):
        sum = abs(a[i] - b[i]) + sum
    return sum
