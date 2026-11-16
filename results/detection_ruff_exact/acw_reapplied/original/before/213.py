def concatenate_strings(test_tup1, test_tup2):
return tuple(ele2 + ele1 for ele1, ele2 in zip(test_tup1, test_tup2))
