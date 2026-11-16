import re

regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def check_email(email):
    if not (re.search(regex, email)):
        return "Invalid Email"
    return "Valid Email"
