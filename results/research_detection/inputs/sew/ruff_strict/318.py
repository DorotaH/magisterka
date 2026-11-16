def max_volume(s):
    maxvalue, i = 0, 1
    for i in range(s - 1):
        j = 1
        for j in range(s):
            k = s - i - j
            maxvalue = max(maxvalue, j * i * k)
    return maxvalue
