def is_Two_Alter(s):
    for i in range(0, len(s) - 2):
        if s[i] != s[i + 2]:
            return False
    if s[0] == s[1]:
        return False
    return True
