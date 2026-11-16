def check_monthnumber(monthname3):
    if not (
        monthname3 == "April"
        or monthname3 == "June"
        or monthname3 == "September"
        or monthname3 == "November"
    ):
        return False
    return True
