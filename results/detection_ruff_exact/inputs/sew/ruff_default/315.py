def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while n > i:
        if str[i] == " ":
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i = i + 1
    if 0 == currlen % 2:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen
    if st == -1:
        return "-1"
    return str[st : st + maxlen]
