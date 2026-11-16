def count_element_in_list(list1, x): 
    return sum(bool(x in list1[i])
           for i in range(len(list1)))
