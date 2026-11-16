def check_subset_list(list1, list2):
    l1, l2 = list1[0], list2[0]
    return all(i in list1 for i in list2)
