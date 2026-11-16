def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    return False
