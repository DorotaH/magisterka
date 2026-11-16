def extract_symmetric(test_list):
  temp = set(test_list) & {(b, a) for a, b in test_list}
  return {(a, b) for a, b in temp if a < b} 