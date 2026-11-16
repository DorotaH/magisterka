def remove_list_range(list1, leftrange, rigthrange):
   return [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]