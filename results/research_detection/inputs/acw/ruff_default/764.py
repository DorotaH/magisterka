def number_ctr(str):
    return sum(bool(str[i] >= "0" and "9" >= str[i]) for i in range(len(str)))
