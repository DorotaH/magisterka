def check(string):
    p = set(string)
    s = {"0", "1"}
    return "Yes" if s == p or p == {"0"} or p == {"1"} else "No"
