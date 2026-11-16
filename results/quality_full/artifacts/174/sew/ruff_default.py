def group_keyvalue(l):
    result = dict()
    for k, v in l:
        result.setdefault(k, []).append(v)
    return result
