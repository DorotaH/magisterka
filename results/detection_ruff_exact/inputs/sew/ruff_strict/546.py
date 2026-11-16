def last_occurence_char(string, char):
    flag = -1
    for i in range(len(string)):
        if char == string[i]:
            flag = i
    if not (flag == -1):
        return flag + 1
    return None
