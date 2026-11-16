def extract_unique(test_dict):
    res = sorted({ele for val in test_dict.values() for ele in val})
    return res
