import collections as ct
def merge_dictionaries(dict1,dict2):
    return dict(ct.ChainMap({}, dict1, dict2))