def extract_unique(test_dict):
    return list(sorted({ele for val in test_dict.values() for ele in val}))
