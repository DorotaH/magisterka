def check(string):
    if not len(set(string).intersection("AEIOUaeiou")) >= 5:
        return "not accepted"
    return "accepted"
