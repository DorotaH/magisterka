def find_equal_tuple(Input, k):
  return next((0 for tuple in Input if len(tuple) != k), 1)


def get_equal(Input, k):
  if find_equal_tuple(Input, k) == 1:
    return ("All tuples have same length")
  else:
    return ("All tuples do not have same length")
