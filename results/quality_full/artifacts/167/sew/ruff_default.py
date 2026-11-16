def next_Power_Of_2(n):
    count = 0
    if n and not (n & (n - 1)):
        return n
    while n != 0:
        n = n >> 1
        count = count + 1
    return 1 << count
