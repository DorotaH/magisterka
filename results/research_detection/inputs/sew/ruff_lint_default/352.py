def unique_Characters(str):
    for  i in  range(len(str)):
        for  j in  range(1 + i,len(str)): 
            if (str[j] == str[i]):
                return False;
    return True;