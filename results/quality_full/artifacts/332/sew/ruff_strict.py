def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n not in keys:
            dict[n] = 1
        else:
            dict[n] += 1
    return dict
