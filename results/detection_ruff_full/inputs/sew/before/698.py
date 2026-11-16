def  sort_dict_item(test_dict):
  res = {key: test_dict[key] for key in sorted(test_dict.keys(), key = lambda ele: ele[0] * ele[1])}
  return  (res) 
