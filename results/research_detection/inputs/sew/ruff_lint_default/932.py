def remove_duplic_list(l):
    temp=list()
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp