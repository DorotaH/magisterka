def is_Two_Alter(s):  
    return next(
        (False for i in range(len(s) - 2) if (s[i] != s[i + 2])), s[0] != s[1]
    )