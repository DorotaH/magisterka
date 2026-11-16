def all_Characters_Same(s):
    n = len(s)
    return all(s[i] == s[0] for i in range(1, n))
