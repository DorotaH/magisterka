def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum((rom_val[s[i]] - 2 * rom_val[s[i - 1]] if i > 0
                    and rom_val[s[i - 1]] < rom_val[s[i]] else rom_val[s[i]])
                   for i in range(len(s)))
