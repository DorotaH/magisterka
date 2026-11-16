def check_monthnumb(monthname2):
    if not (
        monthname2 == "January"
        or monthname2 == "March"
        or monthname2 == "May"
        or monthname2 == "July"
        or monthname2 == "Augest"
        or monthname2 == "October"
        or monthname2 == "December"
    ):
        return False
    else:
        return True
