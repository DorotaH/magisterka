def roman_to_int(s):
    rom_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for i in range(len(s)):
        if not (i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]):
            int_val += rom_val[s[i]]
        else:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
    return int_val
