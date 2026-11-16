
def extract_min_max(test_tup, K):


test_tup = list(test_tup)
temp = sorted(test_tup)
res = [val for idx, val in enumerate(temp) if idx < K or idx >= len(temp) - K]
return tuple(res)
