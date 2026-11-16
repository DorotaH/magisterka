def check(string):
    p = set(string)
    s = {"0", "1"}
    if not (s == p or p == {"0"} or p == {"1"}):
        return "No"
    return "Yes"
