def sum_of_alternates(test_tuple):
  sum1 = 0
  sum2 = 0
  for idx, ele in enumerate(test_tuple):
    if not idx % 2:
      sum2 += ele
    else:
      sum1 += ele
  return (sum1),(sum2) 