def first_Repeated_Char(str):
    h = {}
    for ch in str:
        if ch not in h:
            h[ch] = 0
        else:
            return ch
    return "\0"
