from dateutil.parser import parse
from datetime import timedelta


def task_func(date_str):
    """
    Get the next business day (Mon-Fri) after a certain date string. Implemented by dateutil.parser and datetime.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd" format.

    Returns:
    datetime: The datetime object of the next business day.

    Requirements:
    - datetime
    - dateutil.parser

    Example:
    >>> task_func('2022-10-22')
    datetime.datetime(2022, 10, 24, 0, 0)
    >>> task_func('2022-10-28')
    datetime.datetime(2022, 10, 31, 0, 0)
    """
    given_date = parse(date_str)
    next_day = given_date

    while True:
        next_day = next_day + timedelta(days=1)

        # Monday to Friday are business days
        if 0 <= next_day.weekday() < 5:
            break

    return next_day
