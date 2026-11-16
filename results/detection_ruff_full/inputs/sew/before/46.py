def test_distinct(data):
  if not len(data) == len(set(data)):
    return False;
  else:
    return True
