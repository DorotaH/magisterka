def add_K_element(test_list, K):
    return [tuple(j + K for j in sub) for sub in test_list]
