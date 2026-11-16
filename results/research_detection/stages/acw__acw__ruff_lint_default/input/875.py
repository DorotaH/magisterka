def min_difference(test_list):
temp = [abs(b - a) for a, b in test_list]
return min(temp)
