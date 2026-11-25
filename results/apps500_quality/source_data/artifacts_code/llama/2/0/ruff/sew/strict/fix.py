def is_lucky(year):
    """Check if a year is lucky."""
    for  digit in  str(year):
        if  digit != '0' and  digit != '1' and  digit != '4':
            return  False
    return True


def next_lucky_year(year):
    """Find the next lucky year."""
    year += 1
    while not is_lucky(year):
        year += 1
    return year

current_year=int(input())
next_year=next_lucky_year(current_year)
print(next_year-current_year)
