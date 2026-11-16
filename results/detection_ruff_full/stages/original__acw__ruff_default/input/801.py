def test_three_equal(x, y, z):
    result = set([x, y, z])
    return 0 if len(result) == 3 else 4 - len(result)
