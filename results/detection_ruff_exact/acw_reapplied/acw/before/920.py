def remove_tuple(test_list):


res = [sub for sub in test_list if any(ele != None for ele in sub)]
return (str(res))
