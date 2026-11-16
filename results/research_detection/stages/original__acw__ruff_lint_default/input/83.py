def get_Char(strr):  
    summ = sum((ord(strr[i]) - ord('a') + 1) for i in range(len(strr)))
    if (summ % 26 == 0):
        return ord('z')
    summ = summ % 26
    return chr(ord('a') + summ - 1)