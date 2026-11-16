def zip_tuples(test_tup1, test_tup2):


return [(j, test_tup2[i % len(test_tup2)]) for i, j in enumerate(test_tup1)]
