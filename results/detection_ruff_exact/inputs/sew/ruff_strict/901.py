def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while 1:
        for a in factors:
            if i % a != 0:
                i = i + n
                break
            if factors[-1] == a and i % a == 0:
                return i
