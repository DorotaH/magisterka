import pytz
from dateutil.parser import parse


def task_func(date_str, from_tz, to_tz):
    """
    Convert a date string from one time zone to another and return the time difference in seconds to the current time
    in the destination time zone.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the date string should be converted.

    Returns:
    int: The time difference in seconds.

    Requirements:
    - pytz
    - dateutil.parser
    Example:
    >>> type(task_func('2022-10-22 11:59:59', 'UTC', 'America/Chicago'))
    <class 'int'>
    """
    # Get timezone objects for the source and destination timezones
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)

    # Parse the given date string and localize it to the source timezone
    given_date_naive = parse(date_str)
    given_date = from_tz_obj.localize(given_date_naive)

    # Convert the given date to the destination timezone
    given_date_in_to_tz = given_date.astimezone(to_tz_obj)

    # Get the current time in the destination timezone
    current_date_in_to_tz = datetime.now(pytz.utc).astimezone(to_tz_obj)

    # Calculate the time difference in seconds
    time_difference = current_date_in_to_tz - given_date_in_to_tz

    return int(time_difference.total_seconds())
