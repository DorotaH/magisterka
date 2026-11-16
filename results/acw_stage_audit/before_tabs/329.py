def neg_count(list):
  return sum(bool(0 >= num)
         for num in list)
