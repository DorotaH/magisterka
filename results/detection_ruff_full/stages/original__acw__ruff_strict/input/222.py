def check_type(test_tuple):
    return all(isinstance(ele, type(test_tuple[0])) for ele in test_tuple)
