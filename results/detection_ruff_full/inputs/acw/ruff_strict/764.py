def number_ctr(str):
    return sum(bool(str[i] >= "0" and str[i] <= "9") for i in range(len(str)))
