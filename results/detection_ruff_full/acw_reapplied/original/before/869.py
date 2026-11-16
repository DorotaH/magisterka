def remove_list_range(list1, leftrange, rigthrange):
return [i for i in list1 if (leftrange <= min(i) and rigthrange >= max(i))]
