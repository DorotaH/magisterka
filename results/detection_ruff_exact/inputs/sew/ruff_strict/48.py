def odd_bit_set_number(n):
    count = 0
    res = 0
    temp = n
    while temp > 0:
        if count % 2 == 0:
            res = res | (1 << count)
        count = count + 1
        temp = temp >> 1
    return n | res
