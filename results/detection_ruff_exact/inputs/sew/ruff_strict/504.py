def sum_Of_Series(n):
    sum = 0
    for i in range(1, 1 + n):
        sum = sum + i * i * i
    return sum
