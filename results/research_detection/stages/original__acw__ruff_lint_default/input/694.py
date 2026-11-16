def extract_unique(test_dict):
  return sorted({ele for val in test_dict.values() for ele in val})