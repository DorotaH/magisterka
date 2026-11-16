def dig_let(s):
    d = 0
    l = 0
    for c in s:
        if c.isdigit():
            d = d + 1
        elif c.isalpha():
            l += 1
        else:
            pass
    return l, d
