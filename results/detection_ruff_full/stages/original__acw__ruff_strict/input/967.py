def check(string):
    if len(set(string).intersection("AEIOUaeiou")) >= 5:
        return "accepted"
    return "not accepted"
